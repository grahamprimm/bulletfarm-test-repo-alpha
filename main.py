from flask import Flask, request, jsonify, g
import time
from collections import defaultdict

app = Flask(__name__)

# Rate Limiting Middleware
rate_limit = defaultdict(lambda: {'count': 0, 'timestamp': time.time()})
RATE_LIMIT = 100  # requests per minute

@app.before_request
def limit_requests():
    ip = request.remote_addr
    current_time = time.time()
    data = rate_limit[ip]

    # Reset the counter if a minute has passed
    if current_time - data['timestamp'] > 60:
        data['count'] = 1
        data['timestamp'] = current_time
    else:
        data['count'] += 1

    # Check if limit is exceeded
    if data['count'] > RATE_LIMIT:
        return jsonify({'error': 'Too Many Requests'}), 429

    # Set rate limit headers
    remaining = RATE_LIMIT - data['count']
    g.response.headers['X-RateLimit-Limit'] = str(RATE_LIMIT)
    g.response.headers['X-RateLimit-Remaining'] = str(remaining)

@app.route('/some_endpoint', methods=['GET', 'POST'])
def some_endpoint():
    return jsonify({'message': 'Success'})

if __name__ == '__main__':
    app.run(debug=True)
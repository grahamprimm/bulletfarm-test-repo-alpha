from flask import Flask, request, jsonify
import time
from collections import defaultdict

app = Flask(__name__)

# Rate Limiting Middleware
rate_limit = defaultdict(lambda: {'count': 0, 'timestamp': time.time()})
RATE_LIMIT = 100 # requests per minute

@app.before_request
def limit_requests():
    ip = request.remote_addr
    current_time = time.time()
    data = rate_limit[ip]

    # Reset the counter if a minute has     app.testing = True
    client = app.test_client()

    # Test within limit
    for _ in range(100):
        response = client.post('/some_endpoint')
        assert response.status_code == 200

    # Test exceeding limit
    response = client.post('/some_endpoint')
    assert response.status_code == 429
    assert b'Too Many Requests' in response.data
    assert response.headers['X-RateLimit-Limit'] == '100'
    assert response.headers['X-RateLimit-Remaining'] == '0'ed
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
    response = flask.g.response
    response.headers['X-RateLimit-Limit'] = str(RATE_LIMIT)
    response.headers['X-RateLimit-Remaining'] = str(remaining)

@app.route('/some_endpoint', methods=['GET', 'POST'])
def some_endpoint():
    return jsonify({'message': 'Success'})

if __name__ == '__main__':
    app.run(debug=True)
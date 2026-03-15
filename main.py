from flask import Flask, request, jsonify

app = Flask(__name__)

# Global error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    response = jsonify({'error': 'Internal Server Error'})
    response.status_code = 500
    return response

# Global error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    response = jsonify({'error': 'Resource not found'})
    response.status_code = 404
    return response

# Input validation for POST endpoints
@app.route('/api/resource', methods=['POST'])
def create_resource():
    data = request.get_json()

    # Validate input
    if 'name' not in data or not isinstance(data['name'], str):
        return jsonify({'error': 'Invalid input: name is required and should be a string'}), 400
    if 'price' not in data or not (isinstance(data['price'], (int, float)) and data['price'] > 0):
        return jsonify({'error': 'Invalid input: price is required and should be a positive number'}), 400

    # Proceed with creating the resource
    # ... (resource creation logic goes here)

    return jsonify({'message': 'Resource created successfully'}), 201

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)


def add(a, b):
    return a + b


def multiply(x, y):
    result = x * y
    return result


def divide(numerator, denominator):
    return numerator / denominator


def process_list(items):
    output = []
    for i in items:
        if i > 0:
            output.append(i * 2)
    return output
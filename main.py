# Test cases for Flask API

import pytest
from flask import json
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_internal_error(client):
    response = client.get('/api/nonexistent')  # Trigger a 500 error
    assert response.status_code == 500
    assert response.json['error'] == 'Internal Server Error'


def test_create_data(client):
    # Test successful data creation
    response = client.post('/api/data', json={'data': 'test'})
    assert response.status_code == 201
    assert response.json['message'] == 'Data received'

    # Test missing data field
    response = client.post('/api/data', json={})
    assert response.status_code == 400
    assert response.json['error'] == 'Bad Request'
    assert response.json['message'] == 'Data field is required.'
from flask import Flask, jsonify, request

app = Flask(__name__)

# Custom error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

# Example endpoint
@app.route('/api/data', methods=['POST'])
def create_data():
    # Validate input
    if not request.json or 'data' not in request.json:
        return jsonify({'error': 'Bad Request', 'message': 'Data field is required.'}), 400
    data = request.json['data']
    # Process the data (your logic here)
    return jsonify({'message': 'Data received', 'data': data}), 201

if __name__ == '__main__':
    app.run(debug=True)from flask import Flask, request, jsonify

app = Flask(__name__)

# Global error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    response = jsonify({'error': 'Internal Server Error'})
    response.status_code = 500
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

if __name__ == '__main__':
    app.run(debug=True)def add(a, b):
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

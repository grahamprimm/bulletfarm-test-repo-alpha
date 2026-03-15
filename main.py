from flask import Flask, jsonify, request

app = Flask(__name__)

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

@app.route('/api/resource', methods=['POST'])
def create_resource():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Bad Request', 'message': 'Name is required'}), 400
    # Assuming you process the data and create a new resource
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

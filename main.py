from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data
items = list(range(1, 101))  # List of items from 1 to 100

@app.route('/items', methods=['GET'])
def get_items():
    # Get cursor parameter from query string
    cursor = request.args.get('cursor', default=0, type=int)
    limit = request.args.get('limit', default=10, type=int)

    # Calculate start index based on cursor
    start_index = cursor
    end_index = start_index + limit

    # Get sliced items
    paginated_items = items[start_index:end_index]

    # Create a new cursor for the next page
    next_cursor = end_index if end_index < len(items) else None

    return jsonify({
        'items': paginated_items,
        'next_cursor': next_cursor
    })

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

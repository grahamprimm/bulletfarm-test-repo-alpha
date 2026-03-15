from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(200), nullable=False)

@app.route('/api/items', methods=['GET'])
def get_items():
    cursor = request.args.get('cursor', default=None, type=int)
    limit = request.args.get('limit', default=10, type=int)

    query = Item.query.order_by(Item.id)

    if cursor:
        query = query.filter(Item.id > cursor)

    items = query.limit(limit).all()
    new_cursor = items[-1].id if items else None

    return jsonify({
        'items': [item.data for item in items],
        'next_cursor': new_cursor
    })

if __name__ == '__main__':
    db.create_all()
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

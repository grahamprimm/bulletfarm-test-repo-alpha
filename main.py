from flask import request, jsonify
from math import ceil

class Pagination:
    def __init__(self, items, page, per_page):
        self.items = items
        self.page = page
        self.per_page = per_page
        self.total = len(items)
        self.pages = ceil(self.total / per_page)

    def get_paginated_items(self):
        start = (self.page - 1) * self.per_page
        end = start + self.per_page
        return self.items[start:end]


@app.route('/api/items', methods=['GET'])
def get_items():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    items = get_all_items()  # This should call your data source to fetch items
    pagination = Pagination(items, page, per_page)
    paginated_items = pagination.get_paginated_items()
    return jsonify({
        'items': paginated_items,
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': pagination.page
    })def add(a, b):
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

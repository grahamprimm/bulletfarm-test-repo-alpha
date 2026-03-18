import pytest


def test_internal_error(client):
    response = client.get('/non-existent')
    assert response.status_code == 500
    assert b'Internal Server Error' in response.data


def test_create_resource(client):
    response = client.post('/api/resource', json={})
    assert response.status_code == 400
    assert b'Invalid input' in response.data

    response = client.post('/api/resource', json={'name': 'Test', 'price': -10})
    assert response.status_code == 400
    assert b'Invalid input' in response.data

    response = client.post('/api/resource', json={'name': 'Test', 'price': 10})
    assert response.status_code == 201
    assert b'Resource created successfully' in response.data


def test_add():
    assert add(1, 2) == 3


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(10, 2) == 5


def test_process_list():
    assert process_list([1, -1, 2]) == [2, 4]

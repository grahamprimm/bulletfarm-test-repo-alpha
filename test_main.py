import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_internal_error(client):
    # Test for internal server error
    with pytest.raises(Exception):
        assert app.errorhandler(500)(None)['status_code'] == 500


def test_bad_request(client):
    # Test for bad request error
    response = app.errorhandler(400)(None)
    assert response.status_code == 400


def test_create_resource(client):
    # Test valid POST request
    response = client.post('/api/resource', json={'name': 'Test Resource', 'price': 10.0})
    assert response.status_code == 201
    assert response.json == {'message': 'Resource created successfully'}

    # Test invalid name
    response = client.post('/api/resource', json={'name': 123, 'price': 10.0})
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid input: name is required and should be a string'}

    # Test invalid price
    response = client.post('/api/resource', json={'name': 'Test Resource', 'price': -5})
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid input: price is required and should be a positive number'}


def test_add():
    assert add(1, 2) == 3


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)


def test_process_list():
    assert process_list([1, 2, -1, 3]) == [2, 4, 6]

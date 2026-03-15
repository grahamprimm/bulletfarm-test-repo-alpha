import pytest
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_internal_error(client):
    rv = client.get('/api/non-existing-path')  # Trigger 404 error
    assert rv.status_code == 404
    json_data = rv.get_json()
    assert json_data['error'] == 'Resource not found'


def test_not_found(client):
    rv = client.get('/api/non-existing-path')  # Trigger 404 error
    assert rv.status_code == 404
    json_data = rv.get_json()
    assert json_data['error'] == 'Resource not found'


def test_create_resource(client):
    # Test successful resource creation
    response = client.post('/api/resource', json={'name': 'Test Resource', 'price': 10})
    assert response.status_code == 201
    assert response.get_json()['message'] == 'Resource created successfully'
    
    # Test invalid name
    response = client.post('/api/resource', json={'name': '', 'price': 10})
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Invalid input: name is required and should be a string'

    # Test invalid price
    response = client.post('/api/resource', json={'name': 'Test Resource', 'price': -10})
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Invalid input: price is required and should be a positive number'


def test_add():
    assert add(1, 2) == 3


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(6, 3) == 2


def test_process_list():
    assert process_list([1, 2, -1]) == [2, 4]
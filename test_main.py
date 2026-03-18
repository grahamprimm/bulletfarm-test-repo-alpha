import pytest
from main import app


def test_limit_requests():
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
    assert response.headers['X-RateLimit-Remaining'] == '0'


def test_some_endpoint():
    client = app.test_client()
    response = client.post('/some_endpoint')
    assert response.status_code == 200
    assert response.json == {'message': 'Success'}
import pytest
from flask import Flask
from app import app as foreman_app

@pytest.fixture
def client():
    # Set up the Flask test client
    with foreman_app.test_client() as client:
        yield client

def test_app_initialization():
    assert foreman_app is not None
    assert isinstance(foreman_app, Flask)

def test_route_hello_not_implemented_yet(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'

def test_calc_route(client):
    # Addition
    response_add = client.get('/calc?op=add&x=5&y=3')
    assert response_add.status_code == 200
    assert response_add.json == {'result': 8.0}

    # Subtraction
    response_subtract = client.get('/calc?op=subtract&x=5&y=3')
    assert response_subtract.status_code == 200
    assert response_subtract.json == {'result': 2.0}

    # Multiplication
    response_multiply = client.get('/calc?op=multiply&x=5&y=3')
    assert response_multiply.status_code == 200
    assert response_multiply.json == {'result': 15.0}

    # Division
    response_divide = client.get('/calc?op=divide&x=6&y=2')
    assert response_divide.status_code == 200
    assert response_divide.json == {'result': 3.0}

    # Division by zero
    response_divide_zero = client.get('/calc?op=divide&x=5&y=0')
    assert response_divide_zero.status_code == 400
    assert response_divide_zero.json == {'error': 'Division by zero'}

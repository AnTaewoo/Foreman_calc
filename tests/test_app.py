import pytest
from flask import Flask
from app import app as foreman_app

@pytest.fixture
def client():
    with foreman_app.test_client() as client:
        yield client

def test_app_initialization():
    assert foreman_app is not None
    assert isinstance(foreman_app, Flask)

def test_route_hello_not_implemented_yet(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'

def test_calc_route_add(client):
    response = client.get('/calc?op=add&x=5&y=3')
    assert response.status_code == 200
    assert response.json == {'result': 8.0}

def test_calc_route_subtract(client):
    response = client.get('/calc?op=subtract&x=5&y=3')
    assert response.status_code == 200
    assert response.json == {'result': 2.0}

def test_calc_route_multiply(client):
    response = client.get('/calc?op=multiply&x=5&y=3')
    assert response.status_code == 200
    assert response.json == {'result': 15.0}

def test_calc_route_divide_by_zero(client):
    response = client.get('/calc?op=divide&x=5&y=0')
    assert response.status_code == 400
    assert response.json == {'error': 'Division by zero'}


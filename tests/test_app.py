import pytest
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
    assert response.status_code == 404

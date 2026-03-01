import pytest
from flask import Flask
from app.errors import register_error_handlers

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    register_error_handlers(app)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_404_api_error(client):
    response = client.get('/api/nonexistent')
    assert response.status_code == 404
    data = response.get_json()
    assert data['error']['code'] == 'NOT_FOUND'

def test_404_html_error(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'404' in response.data
    assert b'Page Not Found' in response.data

def test_500_api_error(client):
    @client.application.route('/trigger500')
    def trigger500():
        raise Exception("Test error")
    response = client.get('/trigger500')
    assert response.status_code == 500
    data = response.get_json()
    assert data['error']['code'] == 'INTERNAL_ERROR'

def test_429_rate_limit(client):
    response = client.post('/api/contact', json={'name': 'Test'})
    assert response.status_code == 429
    data = response.get_json()
    assert data['error']['code'] == 'RATE_LIMITED'

import pytest
from flask import url_for
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_download_video(client):
    response = client.post(url_for('download_video'), data={'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'})
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Video downloaded successfully'
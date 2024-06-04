import os
import pytest
from app import app

# Устанавливаем тестовые переменные окружения
os.environ['API_ID'] = 'your_api_id'
os.environ['API_HASH'] = 'your_api_hash'

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_send_message(client):
    response = client.post('/send_message', json={
        'user_id': 'test_user',
        'message': 'Hello, this is a test message!'
    })
    assert response.status_code == 200
    assert response.json == {'status': 'message sent'}

def test_send_media(client):
    response = client.post('/send_media', json={
        'user_id': 'test_user',
        'media_path': 'path/to/media/file.jpg'
    })
    assert response.status_code == 200
    assert response.json == {'status': 'media sent'}

def test_wildberries_search(client):
    response = client.get('/wild?query=test')
    assert response.status_code == 200
    assert 'name' in response.json[0]
    assert 'link' in response.json[0]

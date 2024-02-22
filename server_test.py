from server import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    response = client.get('/index')
    assert response.status_code == 200
    assert b'Events Today' in response.data
    # TODO test weather and food displays


def test_calendar_page(client):
    response = client.get('/calendar')
    assert response.status_code == 200
    assert b'Select Search Method' in response.data
    assert b'calendar-element' in response.data


def test_path_page(client):
    response = client.get('path')
    assert response.status_code == 200
    assert b'Find Path' in response.data


def test_chatroom_page(client):
    response = client.get('/chat')
    assert response.status_code == 200
    assert b'Enter a message: ' in response.data
    assert b'Send' in response.data


def test_path_display_page(client):
    data = {
        'fromBuildingDropdown': '1',
        'toBuildingDropdown': '2'
    }
    response = client.post('/paths/find', data=data)
    assert response.status_code == 200
    assert b'0-1.png' and b'0-2.png' in response.data

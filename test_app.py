import pytest
from app import app  # Import the app instance from your Flask application

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Welcome to Flask!" in response.data  # Updated to match the actual response

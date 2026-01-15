import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI Backend!"}


def test_get_greeting():
    """Test the greeting endpoint returns expected structure"""
    response = client.get("/api/greeting")
    assert response.status_code == 200
    
    data = response.json()
    assert "greeting" in data
    assert "status" in data
    assert data["status"] == "success"
    assert isinstance(data["greeting"], str)
    assert len(data["greeting"]) > 0


def test_get_random_number():
    """Test the random number endpoint returns expected structure"""
    response = client.get("/api/random-number")
    assert response.status_code == 200
    
    data = response.json()
    assert "number" in data
    assert "message" in data
    assert "status" in data
    assert data["status"] == "success"
    assert isinstance(data["number"], int)
    assert 1 <= data["number"] <= 100


def test_get_random_number_range():
    """Test that random numbers are within expected range"""
    # Call multiple times to increase confidence
    for _ in range(10):
        response = client.get("/api/random-number")
        data = response.json()
        assert 1 <= data["number"] <= 100

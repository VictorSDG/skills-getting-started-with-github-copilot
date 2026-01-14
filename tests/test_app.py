import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data

def test_signup_for_activity():
    response = client.post("/activities/Chess Club/signup", params={"email": "newstudent@mergington.edu"})
    assert response.status_code == 200
    assert response.json()["message"] == "Signed up newstudent@mergington.edu for Chess Club"

def test_remove_participant():
    # First, add a participant
    client.post("/activities/Chess Club/signup", params={"email": "removeme@mergington.edu"})
    # Now, remove the participant
    response = client.delete("/activities/Chess Club/participants/removeme@mergington.edu")
    assert response.status_code == 204

from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Task Manager API Running"}

def test_create_task():
    response = client.post("/tasks", json={"title": "Learn CI/CD"})
    assert response.status_code == 200
    assert response.json()["title"] == "Learn CI/CD"
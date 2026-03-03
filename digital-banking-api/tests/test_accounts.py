import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_account():
    response = client.post("/auth/register", json={"email":"a@test.com","password":"pass123"})
    assert response.status_code == 200
    token = response.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/accounts", json={"user_id":1,"balance":5000}, headers=headers)
    assert response.status_code == 200
    assert response.json()["balance"] == 5000
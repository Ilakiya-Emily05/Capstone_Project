import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_transfer():
    response = client.post("/auth/register", json={"email":"b@test.com","password":"pass123"})
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    client.post("/accounts", json={"user_id":2,"balance":10000}, headers=headers)
    client.post("/accounts", json={"user_id":2,"balance":0}, headers=headers)

    tx_data = {"from_account":"<sender_acc_number>","to_account":"<receiver_acc_number>","amount":1000}
    response = client.post("/transactions/transfer", json=tx_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["amount"] == 1000
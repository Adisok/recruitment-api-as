from fastapi.testclient import TestClient
from main import app
import pytest
import sqlite3

client = TestClient(app)

def test_testting():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello Daft!"


def test_auth():
    test_api_token = "BASIC 2cd452177e024c2ef774ab7e7a37254ee4479d81984eb06d7b18d96c0dbf9cfc"
    response = client.post("/token", auth=("Daft_user", "Daft_Password"))
    assert response.status_code == 201
    assert response.json()["api_token"] == test_api_token


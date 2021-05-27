from fastapi.testclient import TestClient
from main import app
import pytest
from starlette.testclient import TestClient



client = TestClient(app)
TOKEN = "BASIC2cd452177e024c2ef774ab7e7a37254ee4479d81984eb06d7b18d96c0dbf9cfc"
TEST_ID = 0


def test_testing():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello Daft!"


def test_auth():
    test_api_token = TOKEN
    response = client.post("/token", auth=("Daft_user", "Daft_Password"))
    assert response.status_code == 201
    assert response.json()["api_token"] == test_api_token


def test_creat_message():
    global TEST_ID
    test_request = {
        "MessageText": "string",
        "Token": "BASIC2cd452177e024c2ef774ab7e7a37254ee4479d81984eb06d7b18d96c0dbf9cfc"
    }
    response = client.post("/create_msg", json=test_request)
    TEST_ID = response.json()["MessageID"]
    print(TEST_ID)
    assert response.json()["MessageText"] == "string"


def test_get_message():
    global TEST_ID
    response = client.get(f"/info_msg/{TEST_ID}")
    assert response.json()["MessageText"] == "string"
    assert response.status_code == 200


def test_edit_message():
    global TEST_ID
    test_edit = {
        "Message": "string",
        "Token": "BASIC2cd452177e024c2ef774ab7e7a37254ee4479d81984eb06d7b18d96c0dbf9cfc"
    }
    response = client.put(f"/edit_msg/{TEST_ID}", json=test_edit)
    assert response.status_code == 201
    assert response.json()["MessageText"] == "string"


def test_delete_message():
    global TEST_ID
    response = client.delete(f"/delete_msg/{TEST_ID}", params={"auth": TOKEN})
    assert response.text == "Deleted!"
    assert response.status_code == 204

import pytest
from src.utils import create_admin
from src.test.config import TestingSessionLocal, client


@pytest.fixture(scope="module")
def session():
    db = TestingSessionLocal()
    create_admin(db)
    yield db
    db.close()


def test_login_success(session):
    res = client.post("/auth/login", json={"username": "admin", "password": "admin123"})
    assert res.status_code == 200
    assert "access_token" in res.json()


def test_login_fail(session):
    res = client.post("/auth/login", json={"username": "admin", "password": "wrong"})
    assert res.status_code == 401


def test_create_user_as_admin(session):
    token = client.post(
        "/auth/login", json={"username": "admin", "password": "admin123"}
    ).json()["access_token"]

    res = client.post(
        "/auth/users",
        headers={"Authorization": f"Bearer {token}"},
        json={"username": "user1", "password": "pass", "roles": "ROLE_USER"},
    )
    assert res.status_code == 201


def test_create_user_no_token(session):
    res = client.post(
        "/auth/users",
        json={"username": "user2", "password": "pass", "roles": "ROLE_USER"},
    )
    assert res.status_code == 403 or res.status_code == 401


def test_user_details(session):
    token = client.post(
        "/auth/login", json={"username": "admin", "password": "admin123"}
    ).json()["access_token"]

    res = client.get("/auth/user_details", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    assert res.json()["sub"] == "admin"

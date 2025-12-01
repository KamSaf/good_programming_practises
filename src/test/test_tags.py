import pytest
from src.models import Tag
from src.queries.tags import load_tags, get_tag_by_id
from src.test.config import TestingSessionLocal, client


@pytest.fixture(scope="module")
def session():
    db = TestingSessionLocal()
    load_tags(db, filename="test_tags.csv")
    yield db
    db.close()


def test_load_tags(session):
    tags = session.query(Tag).all()
    assert len(tags) == 3
    assert tags[0].user_id == 2
    assert tags[0].movie_id == 60756
    assert tags[0].tag == "funny"
    assert tags[0].timestamp == 1445714994

    assert tags[1].user_id == 2
    assert tags[1].movie_id == 60756
    assert tags[1].tag == "Highly quotable"
    assert tags[1].timestamp == 1445714996

    assert tags[2].user_id == 2
    assert tags[2].movie_id == 60756
    assert tags[2].tag == "will ferrell"
    assert tags[2].timestamp == 1445714992


def test_get_tags(session):
    response = client.get("/tags")
    assert response.status_code == 200
    tags = response.json()["tags"]
    assert len(tags) == 3
    assert tags[0]["user_id"] == 2
    assert tags[0]["movie_id"] == 60756
    assert tags[0]["tag"] == "funny"
    assert tags[0]["timestamp"] == 1445714994

    assert tags[1]["user_id"] == 2
    assert tags[1]["movie_id"] == 60756
    assert tags[1]["tag"] == "Highly quotable"
    assert tags[1]["timestamp"] == 1445714996

    assert tags[2]["user_id"] == 2
    assert tags[2]["movie_id"] == 60756
    assert tags[2]["tag"] == "will ferrell"
    assert tags[2]["timestamp"] == 1445714992


def test_get_tag_by_id(session):
    id = 1
    response = client.get(f"/tags/{id}")
    assert response.status_code == 200
    tag = response.json()["tag"]
    assert tag["user_id"] == 2
    assert tag["movie_id"] == 60756
    assert tag["tag"] == "funny"
    assert tag["timestamp"] == 1445714994


def test_add_tag(session):
    id = 4
    payload = {"user_id": 3, "movie_id": 5, "tag": "test_tag", "timestamp": 964982703}
    response = client.post("/tags", json=payload)
    assert response.status_code == 201
    new_tag = get_tag_by_id(id, session)
    assert new_tag
    assert new_tag.id == id
    assert new_tag.user_id == payload["user_id"]
    assert new_tag.movie_id == payload["movie_id"]
    assert new_tag.tag == payload["tag"]
    assert new_tag.timestamp == payload["timestamp"]


def test_update_tag(session):
    id = 4
    payload = {"user_id": 2, "movie_id": 3, "tag": "test_tag_2", "timestamp": 813982703}
    response = client.put(f"/tags/{id}", json=payload)
    assert response.status_code == 200
    new_tag = get_tag_by_id(id, session)
    assert new_tag
    assert new_tag.id == id
    assert new_tag.user_id == payload["user_id"]
    assert new_tag.movie_id == payload["movie_id"]
    assert new_tag.tag == payload["tag"]
    assert new_tag.timestamp == payload["timestamp"]


def test_delete_tag(session):
    id = 4
    response = client.delete(f"/tags/{id}")
    assert response.status_code == 200
    new_tag = get_tag_by_id(id, session)
    assert new_tag is None

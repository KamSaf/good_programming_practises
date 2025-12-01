import pytest
from src.models import Link
from src.queries.links import load_links, get_link_by_id
from src.test.config import TestingSessionLocal, client


@pytest.fixture(scope="module")
def session():
    db = TestingSessionLocal()
    load_links(db, filename="test_links.csv")
    yield db
    db.close()


def test_load_links(session):
    links = session.query(Link).all()
    assert len(links) == 3
    assert links[0].movie_id == 1
    assert links[0].imdb_id == "0114709"
    assert links[0].tmdb_id == "862"

    assert links[1].movie_id == 2
    assert links[1].imdb_id == "0113497"
    assert links[1].tmdb_id == "8844"

    assert links[2].movie_id == 3
    assert links[2].imdb_id == "0113228"
    assert links[2].tmdb_id == "15602"


def test_get_links(session):
    response = client.get("/links")
    assert response.status_code == 200
    links = response.json()["links"]
    assert len(links) == 3
    assert links[0]["movie_id"] == 1
    assert links[0]["imdb_id"] == "0114709"
    assert links[0]["tmdb_id"] == "862"

    assert links[1]["movie_id"] == 2
    assert links[1]["imdb_id"] == "0113497"
    assert links[1]["tmdb_id"] == "8844"

    assert links[2]["movie_id"] == 3
    assert links[2]["imdb_id"] == "0113228"
    assert links[2]["tmdb_id"] == "15602"


def test_get_link_by_id(session):
    id = 1
    response = client.get(f"/links/{id}")
    assert response.status_code == 200
    link = response.json()["link"]
    assert link["movie_id"] == 1
    assert link["imdb_id"] == "0114709"
    assert link["tmdb_id"] == "862"


def test_add_link(session):
    id = 4
    payload = {"movie_id": 5, "imdb_id": "0123456", "tmdb_id": "4432"}
    response = client.post("/links", json=payload)
    assert response.status_code == 201
    new_link = get_link_by_id(id, session)
    assert new_link
    assert new_link.id == id
    assert new_link.movie_id == payload["movie_id"]
    assert new_link.imdb_id == payload["imdb_id"]
    assert new_link.tmdb_id == payload["tmdb_id"]


def test_update_link(session):
    id = 4
    payload = {"movie_id": 7, "imdb_id": "02345678", "tmdb_id": "3244"}
    response = client.put(f"/links/{id}", json=payload)
    assert response.status_code == 200
    new_link = get_link_by_id(id, session)
    assert new_link
    assert new_link.id == id
    assert new_link.movie_id == payload["movie_id"]
    assert new_link.imdb_id == payload["imdb_id"]
    assert new_link.tmdb_id == payload["tmdb_id"]


def test_delete_link(session):
    id = 4
    response = client.delete(f"/links/{id}")
    assert response.status_code == 200
    new_rating = get_link_by_id(id, session)
    assert new_rating is None

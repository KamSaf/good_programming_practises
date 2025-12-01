import pytest
from src.models import Rating
from src.queries.ratings import load_ratings, get_rating_by_id
from src.test.config import TestingSessionLocal, client


@pytest.fixture(scope="module")
def session():
    db = TestingSessionLocal()
    load_ratings(db, filename="test_ratings.csv")
    yield db
    db.close()


def test_load_ratings(session):
    ratings = session.query(Rating).all()
    assert len(ratings) == 3
    assert ratings[0].user_id == 1
    assert ratings[0].movie_id == 1
    assert ratings[0].rating == 4.0
    assert ratings[0].timestamp == 964982703

    assert ratings[1].user_id == 1
    assert ratings[1].movie_id == 3
    assert ratings[1].rating == 4.0
    assert ratings[1].timestamp == 964981247

    assert ratings[2].user_id == 1
    assert ratings[2].movie_id == 6
    assert ratings[2].rating == 4.0
    assert ratings[2].timestamp == 964982224


def test_get_ratings(session):
    response = client.get("/ratings")
    assert response.status_code == 200
    ratings = response.json()["ratings"]
    assert len(ratings) == 3
    assert ratings[0]["user_id"] == 1
    assert ratings[0]["movie_id"] == 1
    assert ratings[0]["rating"] == 4.0
    assert ratings[0]["timestamp"] == 964982703

    assert ratings[1]["user_id"] == 1
    assert ratings[1]["movie_id"] == 3
    assert ratings[1]["rating"] == 4.0
    assert ratings[1]["timestamp"] == 964981247

    assert ratings[2]["user_id"] == 1
    assert ratings[2]["movie_id"] == 6
    assert ratings[2]["rating"] == 4.0
    assert ratings[2]["timestamp"] == 964982224


def test_get_rating_by_id(session):
    id = 1
    response = client.get(f"/ratings/{id}")
    assert response.status_code == 200
    rating = response.json()["rating"]
    assert rating["user_id"] == 1
    assert rating["movie_id"] == 1
    assert rating["rating"] == 4.0
    assert rating["timestamp"] == 964982703


def test_add_rating(session):
    id = 4
    payload = {"user_id": 3, "movie_id": 5, "rating": 5.0, "timestamp": 964982703}
    response = client.post("/ratings", json=payload)
    assert response.status_code == 201
    new_rating = get_rating_by_id(id, session)
    assert new_rating
    assert new_rating.id == id
    assert new_rating.user_id == payload["user_id"]
    assert new_rating.movie_id == payload["movie_id"]
    assert new_rating.rating == payload["rating"]
    assert new_rating.timestamp == payload["timestamp"]


def test_update_rating(session):
    id = 4
    payload = {"user_id": 2, "movie_id": 3, "rating": 3.0, "timestamp": 813982703}
    response = client.put(f"/ratings/{id}", json=payload)
    assert response.status_code == 200
    new_rating = get_rating_by_id(id, session)
    assert new_rating
    assert new_rating.id == id
    assert new_rating.user_id == payload["user_id"]
    assert new_rating.movie_id == payload["movie_id"]
    assert new_rating.rating == payload["rating"]
    assert new_rating.timestamp == payload["timestamp"]


def test_delete_rating(session):
    id = 4
    response = client.delete(f"/ratings/{id}")
    assert response.status_code == 200
    new_rating = get_rating_by_id(id, session)
    assert new_rating is None

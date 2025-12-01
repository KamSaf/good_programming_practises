import pytest
from src.models import Movie
from src.queries.movies import load_movies, get_movie_by_id
from src.test.config import TestingSessionLocal, client


@pytest.fixture(scope="module")
def session():
    db = TestingSessionLocal()
    load_movies(db, filename="test_movies.csv")
    yield db
    db.close()


def test_load_movies(session):
    movies = session.query(Movie).all()
    assert len(movies) == 3
    assert movies[0].title == "test_title_1"
    assert movies[0].genres == "test_genres_1"
    assert movies[1].title == "test_title_2"
    assert movies[1].genres == "test_genres_2"
    assert movies[2].title == "test_title_3"
    assert movies[2].genres == "test_genres_3"


def test_get_movies(session):
    response = client.get("/movies")
    assert response.status_code == 200
    movies = response.json()["movies"]
    assert len(movies) == 3
    assert movies[0]["title"] == "test_title_1"
    assert movies[0]["genres"] == "test_genres_1"
    assert movies[1]["title"] == "test_title_2"
    assert movies[1]["genres"] == "test_genres_2"
    assert movies[2]["title"] == "test_title_3"
    assert movies[2]["genres"] == "test_genres_3"


def test_get_movie_by_id(session):
    id = 1
    response = client.get(f"/movies/{id}")
    assert response.status_code == 200
    movie = response.json()["movie"]
    assert movie["title"] == "test_title_1"
    assert movie["genres"] == "test_genres_1"


def test_add_movie(session):
    id = 4
    payload = {"title": "test_title_4", "genres": "test_title_4"}
    response = client.post("/movies", json=payload)
    assert response.status_code == 201
    new_movie = get_movie_by_id(id, session)
    assert new_movie
    assert new_movie.id == id
    assert new_movie.title == payload["title"]
    assert new_movie.genres == payload["genres"]


def test_update_movie(session):
    id = 4
    payload = {"title": "test_title_4.1", "genres": "test_title_4.1"}
    response = client.put(f"/movies/{id}", json=payload)
    assert response.status_code == 200
    new_movie = get_movie_by_id(id, session)
    assert new_movie
    assert new_movie.id == id
    assert new_movie.title == payload["title"]
    assert new_movie.genres == payload["genres"]


def test_delete_movie(session):
    id = 4
    response = client.delete(f"/movies/{id}")
    assert response.status_code == 200
    new_movie = get_movie_by_id(id, session)
    assert new_movie is None

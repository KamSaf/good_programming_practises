from fastapi import APIRouter
from src.models import Movie, Link, Rating, Tag
from src.utils import read_csv

router = APIRouter()


@router.get("/movies")
def get_movies() -> dict:
    movies = [
        Movie(movie_id, title, genres)
        for [movie_id, title, genres] in read_csv("movies.csv")
    ]
    return {"movies": list(map(lambda m: m.__dict__, movies))}


@router.get("/links")
def get_links() -> dict:
    links = [
        Link(movie_id, imdb_id, tmdb_id)
        for [movie_id, imdb_id, tmdb_id] in read_csv("links.csv")
    ]
    return {"links": list(map(lambda m: m.__dict__, links))}


@router.get("/ratings")
def get_ratings() -> dict:
    ratings = [
        Rating(user_id, movie_id, rating, timestamp)
        for [user_id, movie_id, rating, timestamp] in read_csv("ratings.csv")
    ]
    return {"ratings": list(map(lambda m: m.__dict__, ratings))}


@router.get("/tags")
def get_tags() -> dict:
    tags = [
        Tag(user_id, movie_id, tag, timestamp)
        for [user_id, movie_id, tag, timestamp] in read_csv("tags.csv")
    ]
    return {"tags": list(map(lambda m: m.__dict__, tags))}

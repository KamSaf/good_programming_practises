from fastapi import APIRouter
from src.utils import get_all_movies, get_all_links, get_all_ratings, get_all_tags

router = APIRouter()


@router.get("/movies")
def get_movies() -> dict:
    movies = get_all_movies()
    return {"movies": map(lambda m: m.to_dict(), movies)}


@router.get("/links")
def get_links() -> dict:
    links = get_all_links()
    return {"links": map(lambda m: m.to_dict(), links)}


@router.get("/ratings")
def get_ratings() -> dict:
    ratings = get_all_ratings()
    return {"ratings": map(lambda m: m.to_dict(), ratings)}


@router.get("/tags")
def get_tags() -> dict:
    tags = get_all_tags()
    return {"tags": map(lambda m: m.to_dict(), tags)}

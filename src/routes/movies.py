from fastapi import APIRouter
from src.queries.movies import get_all_movies

router = APIRouter(prefix="/movies")


@router.get("/")
def get_movies() -> dict:
    movies = get_all_movies()
    return {"movies": map(lambda m: m.to_dict(), movies)}


@router.get("/{movie_id}")
def get_movie(movie_id: int) -> dict:
    return {"message": movie_id}


@router.post("/movies")
def add_movie() -> dict:
    return {"message": "work in progress..."}


@router.put("/movies/{movie_id}")
def update_movie() -> dict:
    return {"message": "work in progress..."}


@router.delete("/movies/{movie_id}")
def delete_movie() -> dict:
    return {"message": "work in progress..."}

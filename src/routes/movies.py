from fastapi import APIRouter
from src.utils import get_all_movies

router = APIRouter(prefix="/movies")


@router.get("/")
def get_movies() -> dict:
    movies = get_all_movies()
    return {"movies": map(lambda m: m.to_dict(), movies)}

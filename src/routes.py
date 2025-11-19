from fastapi import APIRouter

router = APIRouter()


@router.get("/movies")
def get_movies() -> dict:
    return {"movies": "work in progress..."}


@router.get("/links")
def get_links() -> dict:
    return {"links": "work in progress..."}


@router.get("/ratings")
def get_ratings() -> dict:
    return {"ratings": "work in progress..."}


@router.get("/tags")
def get_tags() -> dict:
    return {"tags": "work in progress..."}

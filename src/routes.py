from fastapi import APIRouter

router = APIRouter()


@router.get("/movies")
def get_movies() -> dict:
    return {"message": "work in progress..."}


@router.get("/links")
def get_links() -> dict:
    return {"message": "work in progress..."}


@router.get("/ratings")
def get_ratings() -> dict:
    return {"message": "work in progress..."}


@router.get("/tags")
def get_tags() -> dict:
    return {"message": "work in progress..."}

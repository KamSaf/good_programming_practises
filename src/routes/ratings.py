from fastapi import APIRouter
from src.queries.ratings import get_all_ratings

router = APIRouter(prefix="/ratings")


@router.get("/")
def get_ratings() -> dict:
    ratings = get_all_ratings()
    return {"ratings": map(lambda m: m.to_dict(), ratings)}

from fastapi import APIRouter
from src.utils import get_all_tags

router = APIRouter(prefix="/tags")


@router.get("/")
def get_tags() -> dict:
    tags = get_all_tags()
    return {"tags": map(lambda m: m.to_dict(), tags)}

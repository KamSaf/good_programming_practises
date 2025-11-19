from fastapi import APIRouter
from src.utils import get_all_links

router = APIRouter(prefix="/links")


@router.get("/")
def get_links() -> dict:
    links = get_all_links()
    return {"links": map(lambda m: m.to_dict(), links)}

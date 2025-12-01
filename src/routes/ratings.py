from fastapi import APIRouter, Body, Response
from src.queries.ratings import (
    get_all_ratings,
    get_rating_by_id,
    add_rating,
    update_rating_by_id,
    delete_rating_by_id,
)

router = APIRouter(prefix="/ratings")


@router.get("/")
def get_ratings() -> dict:
    ratings = get_all_ratings()
    return {"ratings": map(lambda m: m.to_dict(), ratings)}


@router.get("/{rating_id}", status_code=200)
def get_rating(response: Response, rating_id: int) -> dict:
    rating = get_rating_by_id(rating_id)
    if not rating:
        response.status_code = 404
        return {"message": "Resource not found"}
    return {"rating": rating.to_dict()}


@router.post("/", status_code=201)
def post_rating(response: Response, data: dict = Body(...)) -> dict:
    try:
        add_rating(data)
        return {"message": "Object successfully created."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to save data to database."}


@router.put("/{rating_id}", status_code=200)
def update_rating(rating_id: int, response: Response, data: dict = Body(...)) -> dict:
    try:
        res = update_rating_by_id(rating_id, data)
        if res:
            return {"message": "Object successfully updated."}
        else:
            response.status_code = 404
            return {"message": "Object not found."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to update data to database."}


@router.delete("/{rating_id}", status_code=200)
def delete_rating(rating_id: int, response: Response) -> dict:
    try:
        res = delete_rating_by_id(rating_id)
        if res:
            return {"message": "Object successfully deleted."}
        else:
            response.status_code = 404
            return {"message": "Object not found."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to delete data to database."}

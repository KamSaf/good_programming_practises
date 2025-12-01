from fastapi import APIRouter, Body, Response, Depends
from sqlalchemy.orm import Session
from src.config import get_db
from src.queries.movies import (
    get_all_movies,
    get_movie_by_id,
    add_movie,
    delete_movie_by_id,
    update_movie_by_id,
)

router = APIRouter(prefix="/movies")


@router.get("/", status_code=200)
def get_movies(db: Session = Depends(get_db)) -> dict:
    movies = get_all_movies(db)
    return {"movies": map(lambda m: m.to_dict(), movies)}


@router.get("/{movie_id}", status_code=200)
def get_movie(response: Response, movie_id: int, db: Session = Depends(get_db)) -> dict:
    movie = get_movie_by_id(movie_id, db)
    if not movie:
        response.status_code = 404
        return {"message": "Resource not found"}
    return {"movie": movie.to_dict()}


@router.post("/", status_code=201)
def post_movie(
    response: Response, data: dict = Body(...), db: Session = Depends(get_db)
) -> dict:
    try:
        add_movie(data, db)
        return {"message": "Object successfully created."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to save data to database."}


@router.put("/{movie_id}", status_code=200)
def update_movie(
    movie_id: int,
    response: Response,
    data: dict = Body(...),
    db: Session = Depends(get_db),
) -> dict:
    try:
        res = update_movie_by_id(movie_id, data, db)
        if res:
            return {"message": "Object successfully updated."}
        else:
            response.status_code = 404
            return {"message": "Object not found."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to update data to database."}


@router.delete("/{movie_id}", status_code=200)
def delete_movie(
    movie_id: int, response: Response, db: Session = Depends(get_db)
) -> dict:
    try:
        res = delete_movie_by_id(movie_id, db)
        if res:
            return {"message": "Object successfully deleted."}
        else:
            response.status_code = 404
            return {"message": "Object not found."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to delete data to database."}

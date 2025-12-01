from fastapi import APIRouter, Body, Response, Depends
from sqlalchemy.orm import Session
from src.config import get_db
from src.queries.links import (
    get_all_links,
    get_link_by_id,
    add_link,
    update_link_by_id,
    delete_link_by_id,
)

router = APIRouter(prefix="/links")


@router.get("/")
def get_links(db: Session = Depends(get_db)) -> dict:
    links = get_all_links(db)
    return {"links": map(lambda m: m.to_dict(), links)}


@router.get("/{link_id}", status_code=200)
def get_link(response: Response, link_id: int, db: Session = Depends(get_db)) -> dict:
    link = get_link_by_id(link_id, db)
    if not link:
        response.status_code = 404
        return {"message": "Resource not found"}
    return {"link": link.to_dict()}


@router.post("/", status_code=201)
def post_link(
    response: Response, data: dict = Body(...), db: Session = Depends(get_db)
) -> dict:
    try:
        add_link(data, db)
        return {"message": "Object successfully created."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to save data to database."}


@router.put("/{link_id}", status_code=200)
def update_link(
    link_id: int,
    response: Response,
    data: dict = Body(...),
    db: Session = Depends(get_db),
) -> dict:
    try:
        res = update_link_by_id(link_id, data, db)
        if res:
            return {"message": "Object successfully updated."}
        else:
            response.status_code = 404
            return {"message": "Object not found."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to update data to database."}


@router.delete("/{link_id}", status_code=200)
def delete_link(
    link_id: int, response: Response, db: Session = Depends(get_db)
) -> dict:
    try:
        res = delete_link_by_id(link_id, db)
        if res:
            return {"message": "Object successfully deleted."}
        else:
            response.status_code = 404
            return {"message": "Object not found."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to delete data to database."}

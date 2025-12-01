from fastapi import APIRouter, Body, Response
from src.queries.links import (
    get_all_links,
    get_link_by_id,
    add_link,
    update_link_by_id,
    delete_link_by_id,
)

router = APIRouter(prefix="/links")


@router.get("/")
def get_links() -> dict:
    links = get_all_links()
    return {"links": map(lambda m: m.to_dict(), links)}


@router.get("/{link_id}", status_code=200)
def get_link(response: Response, link_id: int) -> dict:
    link = get_link_by_id(link_id)
    if not link:
        response.status_code = 404
        return {"message": "Resource not found"}
    return {"link": link.to_dict()}


@router.post("/", status_code=201)
def post_link(response: Response, data: dict = Body(...)) -> dict:
    try:
        add_link(data)
        return {"message": "Object successfully created."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to save data to database."}


@router.put("/{link_id}", status_code=200)
def update_link(link_id: int, response: Response, data: dict = Body(...)) -> dict:
    try:
        res = update_link_by_id(link_id, data)
        if res:
            return {"message": "Object successfully updated."}
        else:
            response.status_code = 404
            return {"message": "Object not found."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to update data to database."}


@router.delete("/{link_id}", status_code=200)
def delete_link(link_id: int, response: Response) -> dict:
    try:
        res = delete_link_by_id(link_id)
        if res:
            return {"message": "Object successfully deleted."}
        else:
            response.status_code = 404
            return {"message": "Object not found."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to delete data to database."}

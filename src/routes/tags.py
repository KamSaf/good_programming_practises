from fastapi import APIRouter, Body, Response
from src.queries.tags import (
    get_all_tags,
    get_tag_by_id,
    add_tag,
    update_tag_by_id,
    delete_tag_by_id,
)

router = APIRouter(prefix="/tags")


@router.get("/")
def get_tags() -> dict:
    tags = get_all_tags()
    return {"tags": map(lambda m: m.to_dict(), tags)}


@router.get("/{tag_id}", status_code=200)
def get_tag(response: Response, tag_id: int) -> dict:
    tag = get_tag_by_id(tag_id)
    if not tag:
        response.status_code = 404
        return {"message": "Resource not found"}
    return {"tag": tag.to_dict()}


@router.post("/", status_code=201)
def post_tag(response: Response, data: dict = Body(...)) -> dict:
    try:
        add_tag(data)
        return {"message": "Object successfully created."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to save data to database."}


@router.put("/{tag_id}", status_code=200)
def update_tag(tag_id: int, response: Response, data: dict = Body(...)) -> dict:
    try:
        res = update_tag_by_id(tag_id, data)
        if res:
            return {"message": "Object successfully updated."}
        else:
            response.status_code = 404
            return {"message": "Object not found."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to update data to database."}


@router.delete("/{tag_id}", status_code=200)
def delete_tag(tag_id: int, response: Response) -> dict:
    try:
        res = delete_tag_by_id(tag_id)
        if res:
            return {"message": "Object successfully deleted."}
        else:
            response.status_code = 404
            return {"message": "Object not found."}
    except Exception:
        response.status_code = 500
        return {"message": "Error occured when trying to delete data to database."}

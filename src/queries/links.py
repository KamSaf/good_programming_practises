from typing import Sequence
from sqlalchemy.orm import Session
from src.models import Link
from sqlalchemy import select
from src.utils import read_csv, parse_link_data


def load_links(db: Session, filename: str = "links.csv"):
    links = [
        Link(
            movie_id=movie_id,
            imdb_id=int(imdb_id) if imdb_id else None,
            tmdb_id=int(tmdb_id) if tmdb_id else None,
        )
        for [movie_id, imdb_id, tmdb_id] in read_csv(filename)
    ]
    db.add_all(links)
    db.commit()


def get_all_links(db: Session) -> Sequence[Link]:
    stmt = select(Link)
    result = db.scalars(stmt)
    return result.all()


def get_link_by_id(link_id: int, db: Session) -> Link | None:
    stmt = select(Link).where(Link.id == link_id)
    result = db.scalars(stmt).all()
    return result[0] if len(result) > 0 else None


def add_link(link_data: dict, db: Session) -> None:
    link = parse_link_data(link_data)
    db.add_all([link])
    db.commit()


def delete_link_by_id(link_id: int, db: Session) -> bool:
    stmt = select(Link).where(Link.id == link_id)
    result = db.scalars(stmt)
    obj = result.first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True


def update_link_by_id(link_id: int, link_data: dict, db: Session) -> bool:
    stmt = select(Link).where(Link.id == link_id)
    link = parse_link_data(link_data)
    result = db.scalars(stmt)
    obj = result.first()
    if not obj:
        return False
    obj.movie_id = link.movie_id
    obj.imdb_id = link.imdb_id
    obj.tmdb_id = link.tmdb_id
    db.commit()
    return True

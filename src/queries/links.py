from typing import Sequence
from sqlalchemy.orm import Session
from src.config import engine
from src.models import Link
from sqlalchemy import select
from src.utils import read_csv, parse_link_data


def load_links(filename: str = "links.csv"):
    with Session(engine) as session:
        links = [
            Link(
                movie_id=movie_id,
                imdb_id=int(imdb_id) if imdb_id else None,
                tmdb_id=int(tmdb_id) if tmdb_id else None,
            )
            for [movie_id, imdb_id, tmdb_id] in read_csv(filename)
        ]
        session.add_all(links)
        session.commit()


def get_all_links() -> Sequence[Link]:
    stmt = select(Link)
    with Session(engine) as session:
        result = session.scalars(stmt)
        return result.all()


def get_link_by_id(link_id: int) -> Link | None:
    stmt = select(Link).where(Link.id == link_id)
    with Session(engine) as session:
        result = session.scalars(stmt)
        return result.all()[0] if len(result.all()) > 0 else None


def add_link(link_data: dict) -> None:
    link = parse_link_data(link_data)
    with Session(engine) as session:
        session.add_all([link])
        session.commit()


def delete_link_by_id(link_id: int) -> bool:
    stmt = select(Link).where(Link.id == link_id)
    with Session(engine) as session:
        result = session.scalars(stmt)
        obj = result.first()
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True


def update_link_by_id(link_id: int, link_data: dict) -> bool:
    stmt = select(Link).where(Link.id == link_id)
    link = parse_link_data(link_data)
    with Session(engine) as session:
        result = session.scalars(stmt)
        obj = result.first()
        if not obj:
            return False
        obj.movie_id = link.movie_id
        obj.imdb_id = link.imdb_id
        obj.tmdb_id = link.tmdb_id
        session.commit()
        return True

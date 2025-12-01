from typing import Sequence
from sqlalchemy.orm import Session
from src.config import engine
from src.models import Tag
from sqlalchemy import select
from src.utils import read_csv, parse_tag_data


def load_tags(filename: str = "tags.csv"):
    with Session(engine) as session:
        tags = [
            Tag(
                user_id=int(user_id),
                movie_id=int(movie_id),
                tag=tag,
                timestamp=int(timestamp),
            )
            for [user_id, movie_id, tag, timestamp] in read_csv(filename)
        ]
        session.add_all(tags)
        session.commit()


def get_all_tags() -> Sequence[Tag]:
    stmt = select(Tag)
    with Session(engine) as session:
        result = session.scalars(stmt)
        return result.all()


def get_tag_by_id(tag_id: int) -> Tag | None:
    stmt = select(Tag).where(Tag.id == tag_id)
    with Session(engine) as session:
        result = session.scalars(stmt)
        return result.all()[0] if len(result.all()) > 0 else None


def add_tag(tag_data: dict) -> None:
    tag = parse_tag_data(tag_data)
    with Session(engine) as session:
        session.add_all([tag])
        session.commit()


def delete_tag_by_id(tag_id: int) -> bool:
    stmt = select(Tag).where(Tag.id == tag_id)
    with Session(engine) as session:
        result = session.scalars(stmt)
        obj = result.first()
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True


def update_tag_by_id(tag_id: int, tag_data: dict) -> bool:
    stmt = select(Tag).where(Tag.id == tag_id)
    tag = parse_tag_data(tag_data)
    with Session(engine) as session:
        result = session.scalars(stmt)
        obj = result.first()
        if not obj:
            return False
        obj.user_id = tag.user_id
        obj.movie_id = tag.movie_id
        obj.tag = tag.tag
        obj.timestamp = tag.timestamp
        session.commit()
        return True

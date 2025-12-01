from typing import Sequence
from sqlalchemy.orm import Session
from src.models import Tag
from sqlalchemy import select
from src.utils import read_csv, parse_tag_data


def load_tags(db: Session, filename: str = "tags.csv"):
    tags = [
        Tag(
            user_id=int(user_id),
            movie_id=int(movie_id),
            tag=tag,
            timestamp=int(timestamp),
        )
        for [user_id, movie_id, tag, timestamp] in read_csv(filename)
    ]
    db.add_all(tags)
    db.commit()


def get_all_tags(db: Session) -> Sequence[Tag]:
    stmt = select(Tag)
    result = db.scalars(stmt)
    return result.all()


def get_tag_by_id(tag_id: int, db: Session) -> Tag | None:
    stmt = select(Tag).where(Tag.id == tag_id)
    result = db.scalars(stmt).all()
    return result[0] if len(result) > 0 else None


def add_tag(tag_data: dict, db: Session) -> None:
    tag = parse_tag_data(tag_data)
    db.add_all([tag])
    db.commit()


def delete_tag_by_id(tag_id: int, db: Session) -> bool:
    stmt = select(Tag).where(Tag.id == tag_id)
    result = db.scalars(stmt)
    obj = result.first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True


def update_tag_by_id(tag_id: int, tag_data: dict, db: Session) -> bool:
    stmt = select(Tag).where(Tag.id == tag_id)
    tag = parse_tag_data(tag_data)
    result = db.scalars(stmt)
    obj = result.first()
    if not obj:
        return False
    obj.user_id = tag.user_id
    obj.movie_id = tag.movie_id
    obj.tag = tag.tag
    obj.timestamp = tag.timestamp
    db.commit()
    return True

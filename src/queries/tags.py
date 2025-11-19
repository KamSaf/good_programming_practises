from typing import Sequence
from sqlalchemy.orm import Session
from src.config import engine
from src.models import Tag
from sqlalchemy import select
from src.utils import read_csv


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

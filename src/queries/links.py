from typing import Sequence
from sqlalchemy.orm import Session
from src.config import engine
from src.models import Link
from sqlalchemy import select
from src.utils import read_csv


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

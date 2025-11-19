from typing import Sequence
from sqlalchemy.orm import Session
from src.config import engine
from src.models import Movie
from sqlalchemy import select
from src.utils import read_csv


def load_movies(filename: str = "movies.csv") -> None:
    with Session(engine) as session:
        movies = [
            Movie(id=int(movie_id), title=title, genres=genres)
            for [movie_id, title, genres] in read_csv(filename)
        ]
        session.add_all(movies)
        session.commit()


def get_all_movies() -> Sequence[Movie]:
    stmt = select(Movie)
    with Session(engine) as session:
        result = session.scalars(stmt)
        return result.all()

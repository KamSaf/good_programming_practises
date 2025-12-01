from typing import Sequence
from sqlalchemy.orm import Session
from src.config import engine
from src.models import Movie
from sqlalchemy import select
from src.utils import read_csv, parse_movie_data


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


def get_movie_by_id(movie_id: int) -> Movie | None:
    stmt = select(Movie).where(Movie.id == movie_id)
    with Session(engine) as session:
        result = session.scalars(stmt)
        return result.all()[0] if len(result.all()) > 0 else None


def add_movie(movie_data: dict) -> None:
    movie = parse_movie_data(movie_data)
    with Session(engine) as session:
        session.add_all([movie])
        session.commit()


def delete_movie_by_id(movie_id: int) -> bool:
    stmt = select(Movie).where(Movie.id == movie_id)
    with Session(engine) as session:
        result = session.scalars(stmt)
        obj = result.first()
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True


def update_movie_by_id(movie_id: int, movie_data: dict) -> bool:
    stmt = select(Movie).where(Movie.id == movie_id)
    movie = parse_movie_data(movie_data)
    with Session(engine) as session:
        result = session.scalars(stmt)
        obj = result.first()
        if not obj:
            return False
        obj.title = movie.title
        obj.genres = movie.genres
        session.commit()
        return True

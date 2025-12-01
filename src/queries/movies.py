from typing import Sequence
from sqlalchemy.orm import Session
from src.models import Movie
from sqlalchemy import select
from src.utils import read_csv, parse_movie_data


def load_movies(db: Session, filename: str = "movies.csv") -> None:
    movies = [
        Movie(id=int(movie_id), title=title, genres=genres)
        for [movie_id, title, genres] in read_csv(filename)
    ]
    db.add_all(movies)
    db.commit()


def get_all_movies(db: Session) -> Sequence[Movie]:
    stmt = select(Movie)
    result = db.scalars(stmt)
    return result.all()


def get_movie_by_id(movie_id: int, db: Session) -> Movie | None:
    stmt = select(Movie).where(Movie.id == movie_id)
    result = db.scalars(stmt).all()
    return result[0] if len(result) > 0 else None


def add_movie(movie_data: dict, db: Session) -> None:
    movie = parse_movie_data(movie_data)
    db.add_all([movie])
    db.commit()


def delete_movie_by_id(movie_id: int, db: Session) -> bool:
    stmt = select(Movie).where(Movie.id == movie_id)
    result = db.scalars(stmt)
    obj = result.first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True


def update_movie_by_id(movie_id: int, movie_data: dict, db: Session) -> bool:
    stmt = select(Movie).where(Movie.id == movie_id)
    movie = parse_movie_data(movie_data)
    result = db.scalars(stmt)
    obj = result.first()
    if not obj:
        return False
    obj.title = movie.title
    obj.genres = movie.genres
    db.commit()
    return True

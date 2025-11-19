import csv
from typing import Sequence
from sqlalchemy.orm import Session
from src.config import ROOT, engine
from src.models import Movie, Link, Rating, Tag
from sqlalchemy import select


def read_csv(filename: str) -> list[list[str]]:
    path = ROOT / "db" / filename
    with open(path, "r") as read_file:
        next(read_file)
        return [row for row in csv.reader(read_file)]


def load_movies(filename: str = "movies.csv") -> None:
    with Session(engine) as session:
        movies = [
            Movie(id=int(movie_id), title=title, genres=genres)
            for [movie_id, title, genres] in read_csv(filename)
        ]
        session.add_all(movies)
        session.commit()


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


def load_ratings(filename: str = "ratings.csv"):
    with Session(engine) as session:
        ratings = [
            Rating(
                user_id=int(user_id),
                movie_id=int(movie_id),
                rating=float(rating),
                timestamp=int(timestamp),
            )
            for [user_id, movie_id, rating, timestamp] in read_csv(filename)
        ]
        session.add_all(ratings)
        session.commit()


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


def get_all_movies() -> Sequence[Movie]:
    stmt = select(Movie)
    with Session(engine) as session:
        result = session.scalars(stmt)
        return result.all()


def get_all_links() -> Sequence[Link]:
    stmt = select(Link)
    with Session(engine) as session:
        result = session.scalars(stmt)
        return result.all()


def get_all_ratings() -> Sequence[Rating]:
    stmt = select(Rating)
    with Session(engine) as session:
        result = session.scalars(stmt)
        return result.all()


def get_all_tags() -> Sequence[Tag]:
    stmt = select(Tag)
    with Session(engine) as session:
        result = session.scalars(stmt)
        return result.all()

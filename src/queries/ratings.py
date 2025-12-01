from typing import Sequence
from sqlalchemy.orm import Session
from src.config import engine
from src.models import Rating
from sqlalchemy import select
from src.utils import read_csv, parse_rating_data


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


def get_all_ratings() -> Sequence[Rating]:
    stmt = select(Rating)
    with Session(engine) as session:
        result = session.scalars(stmt)
        return result.all()


def get_rating_by_id(rating_id: int) -> Rating | None:
    stmt = select(Rating).where(Rating.id == rating_id)
    with Session(engine) as session:
        result = session.scalars(stmt)
        return result.all()[0] if len(result.all()) > 0 else None


def add_rating(rating_data: dict) -> None:
    rating = parse_rating_data(rating_data)
    with Session(engine) as session:
        session.add_all([rating])
        session.commit()


def delete_rating_by_id(rating_id: int) -> bool:
    stmt = select(Rating).where(Rating.id == rating_id)
    with Session(engine) as session:
        result = session.scalars(stmt)
        obj = result.first()
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True


def update_rating_by_id(rating_id: int, rating_data: dict) -> bool:
    stmt = select(Rating).where(Rating.id == rating_id)
    rating = parse_rating_data(rating_data)
    with Session(engine) as session:
        result = session.scalars(stmt)
        obj = result.first()
        if not obj:
            return False
        obj.user_id = rating.user_id
        obj.movie_id = rating.movie_id
        obj.rating = rating.rating
        obj.timestamp = rating.timestamp
        session.commit()
        return True

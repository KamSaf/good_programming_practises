from typing import Sequence
from sqlalchemy.orm import Session
from src.models import Rating
from sqlalchemy import select
from src.utils import read_csv, parse_rating_data


def load_ratings(db: Session, filename: str = "ratings.csv"):
    ratings = [
        Rating(
            user_id=int(user_id),
            movie_id=int(movie_id),
            rating=float(rating),
            timestamp=int(timestamp),
        )
        for [user_id, movie_id, rating, timestamp] in read_csv(filename)
    ]
    db.add_all(ratings)
    db.commit()


def get_all_ratings(db: Session) -> Sequence[Rating]:
    stmt = select(Rating)
    result = db.scalars(stmt)
    return result.all()


def get_rating_by_id(rating_id: int, db: Session) -> Rating | None:
    stmt = select(Rating).where(Rating.id == rating_id)
    result = db.scalars(stmt).all()
    return result[0] if len(result) > 0 else None


def add_rating(rating_data: dict, db: Session) -> None:
    rating = parse_rating_data(rating_data)
    db.add_all([rating])
    db.commit()


def delete_rating_by_id(rating_id: int, db: Session) -> bool:
    stmt = select(Rating).where(Rating.id == rating_id)
    result = db.scalars(stmt)
    obj = result.first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True


def update_rating_by_id(rating_id: int, rating_data: dict, db: Session) -> bool:
    stmt = select(Rating).where(Rating.id == rating_id)
    rating = parse_rating_data(rating_data)
    result = db.scalars(stmt)
    obj = result.first()
    if not obj:
        return False
    obj.user_id = rating.user_id
    obj.movie_id = rating.movie_id
    obj.rating = rating.rating
    obj.timestamp = rating.timestamp
    db.commit()
    return True

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional
from sqlalchemy import String, Integer, Float, ForeignKey


class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = "movie"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    genres: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        return (
            f"Movie(movie_id={self.id!r}, title={self.title!r}, genres={self.genres!r})"
        )


class Link(Base):
    __tablename__ = "link"
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"))
    imdb_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey=True)
    tmdb_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey=True)

    def __repr__(self) -> str:
        return f"Link(movie_id={self.movie_id!r}, imdb_id={self.imdb_id!r}, tmdb_id={self.tmdb_id!r})"


class Rating(Base):
    __tablename__ = "rating"
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"))
    rating: Mapped[float] = mapped_column(Float)
    timestamp: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"Rating(user_id={self.user_id!r}, movie_id={self.movie_id!r}, rating={self.rating!r}, timestamp={self.timestamp!r})"


class Tag:
    __tablename__ = "tag"
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"))
    tag: Mapped[String] = mapped_column(String(50))
    timestamp: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return f"Tag(user_id={self.user_id!r}, movie_id={self.movie_id!r}, tag={self.tag!r}, timestamp={self.timestamp!r})"

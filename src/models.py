class Movie:
    def __init__(self, movie_id: int, title: str, genres: str) -> None:
        movie_id = movie_id
        title = title
        genres = genres


class Link:
    def __init__(self, movie_id: int, imdb_id: int, tmdb_id: int) -> None:
        movie_id = movie_id
        imdb_id = imdb_id
        tmdb_id = tmdb_id


class Rating:
    def __init__(
        self, user_id: int, movie_id: int, rating: float, timestamp: int
    ) -> None:
        user_id = user_id
        movie_id = movie_id
        rating = rating
        timestamp = timestamp


class Tag:
    def __init__(self, user_id: int, movie_id: int, tag: str, timestamp: int) -> None:
        user_id = user_id
        movie_id = movie_id
        tag = tag
        timestamp = timestamp

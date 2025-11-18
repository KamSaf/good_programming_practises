class Movie:
    def __init__(self, movie_id: str, title: str, genres: str) -> None:
        self.movie_id = int(movie_id)
        self.title = title
        self.genres = genres


class Link:
    def __init__(self, movie_id: str, imdb_id: str, tmdb_id: str) -> None:
        self.movie_id = int(movie_id)
        self.imdb_id = int(imdb_id) if imdb_id else None
        self.tmdb_id = int(tmdb_id) if tmdb_id else None


class Rating:
    def __init__(
        self, user_id: str, movie_id: str, rating: str, timestamp: str
    ) -> None:
        self.user_id = int(user_id)
        self.movie_id = int(movie_id)
        self.rating = float(rating)
        self.timestamp = int(timestamp)


class Tag:
    def __init__(self, user_id: str, movie_id: str, tag: str, timestamp: str) -> None:
        self.user_id = int(user_id)
        self.movie_id = int(movie_id)
        self.tag = tag
        self.timestamp = int(timestamp)

from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all_movies(self, filters):
        """
            Получение всех фильмов
        """
        if filters.get("director_id") is not None:
            movies = self.dao.get_movie_by_director(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_movie_by_genre(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_movie_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all_movies()
        return movies

    def get_one_movie(self, mid):
        """
            Получение фильма по id
        """
        return self.dao.get_one_movie(mid)

    def create_movie(self, movie_data):
        """
            Создание фильма
        """
        return self.dao.create_movie(movie_data)


    def update_movie(self, movie_data):
        """
            Обновление данных о фильме
        """
        return self.dao.update_movie(movie_data)

    def delete_movie(self, mid):
        """
            Удаление фильма
        """
        self.dao.delete_movie(mid)

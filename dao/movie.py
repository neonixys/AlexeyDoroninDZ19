from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        """
            Получение всех фильмов
        """
        return self.session.query(Movie).all()

    def get_one_movie(self, mid):
        """
            Получение фильма по id
        """
        return self.session.query(Movie).get(mid)

    def create_movie(self, movie_data):
        """
            Создание фильма
        """
        movie = Movie(**movie_data)
        self.session.add(movie)
        self.session.commit()
        return movie



    def get_movie_by_director(self, did):
        """
            Получение фильмов по режиссеру
        """
        return self.session.query(Movie).filter(Movie.director_id == did)

    def get_movie_by_genre(self, gid):
        """
            Получение фильмов по жанру
        """
        return self.session.query(Movie).filter(Movie.genre_id == gid)

    def get_movie_by_year(self, yid):
        """
            Получение фильмов по году
        """
        return self.session.query(Movie).filter(Movie.year == yid)

    def update_movie(self, movie_data):
        """
            Обновление фильма
        """
        mid = movie_data.get('id')

        self.session.query(Movie).filter(Movie.id == mid).update(movie_data)
        self.session.commit()

    def delete_movie(self, mid):
        """
            Удаление фильма
        """
        movie = self.get_one_movie(mid)
        self.session.delete(movie)
        self.session.commit()

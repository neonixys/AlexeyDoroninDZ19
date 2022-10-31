from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        """
            Получение всех жанров
        """
        return self.session.query(Genre).all()

    def get_one_genre(self, gid):
        """
            Получение жанра по id
        """
        return self.session.query(Genre).filter(Genre.id == gid).one()

    def create_genre(self, genre_data):
        """
            Создание жанра
        """
        genre = Genre(**genre_data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update_genre(self, genre_data):
        """
            Обновление жанра
        """
        genre = genre_data.get('id')
        self.session.query(Genre).filter(Genre.id == genre).update(genre_data)
        self.session.commit()

    def delete_genre(self, gid):
        """
            Удаление жанра
        """
        genre = self.get_one_genre(gid)
        self.session.delete(genre)
        self.session.commit()


from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all_genres(self):
        """
            Получение всех жанров
        """
        return self.dao.get_all_genres()

    def get_one_genre(self, gid):
        """
            Получение жанра по id
        """
        return self.dao.get_one_genre(gid)

    def create_genre(self, genre_data):
        """
            Создание жанра
        """
        return self.dao.create_genre(genre_data)

    def update_genre(self, genre_data):
        """
            Обновление данных о жанре
        """
        return self.dao.update_genre(genre_data)

    def delete_genre(self, gid):
        """
            Удаление жанра
        """
        self.dao.delete_genre(gid)

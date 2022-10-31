from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all_directors(self):
        """
            Получение всех режиссеров
        """
        return self.dao.get_all_directors()

    def get_one_director(self, did):
        """
            Получение режиссера по id
        """
        return self.dao.get_one_director(did)

    def create_director(self, director_data):
        """
            Создание режиссера
        """
        return self.dao.create_director(director_data)

    def update_director(self, director_data):
        """
            Обновление данных о режиссере
        """
        return self.dao.update_director(director_data)

    def delete_director(self, did):
        """
            Удаление режиссера
        """
        self.dao.delete_director(did)
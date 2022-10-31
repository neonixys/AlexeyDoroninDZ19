from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        """
            Получение всех режиссеров
        """
        return self.session.query(Director).all()

    def get_one_director(self, did):
        """
            Получение режиссера по id
        """
        return self.session.query(Director).filter(Director.id == did).one()


    def create_director(self, director_data):
        """
            Добавление режиссера
        """
        director = Director(**director_data)
        self.session.add(director)
        self.session.commit()
        return director


    def update_director(self, director_data):
        """
            Обновление данных режиссера
        """
        director = director_data.get('id')
        self.session.query(Director).filter(Director.id == director).update(director_data)
        self.session.commit()

    def delete_director(self, did):
        """
            Удаление режиссера
        """
        director = self.get_one_director(did)
        self.session.delete(director)
        self.session.commit()

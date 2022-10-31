from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all_users(self):
        """
            Получение всех пользователей
        """
        return self.session.query(User).all()

    def get_user_by_username(self, username):
        """
            Получение пользователя по username
        """
        return self.session.query(User).filter(User.username == username).first()


    def create_user(self, user_data):
        """
            Создание пользователя
        """
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()
        return user

    def update_user(self, data, username):
        """
            Обновление пользователя
        """
        self.session.query(User).filter(User.username == username).update(data)
        self.session.commit()

    def delete_user(self, username):
        """
            Удаление пользователя
        """
        user = self.get_user_by_username(username)
        self.session.delete(user)
        self.session.commit()

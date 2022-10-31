from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from decorators import auth_required, admin_required
from implemented import genre_service

genre_ns = Namespace('genres')
# Формирование сереилизаторов для модели Genres для одного элемента и для спи
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenreViews(Resource):
    @auth_required
    def get(self):
        """
            Формирование представления для получения жанров
        """
        query = genre_service.get_all_genres()
        return genres_schema.dump(query)

    @admin_required
    def post(self):
        """
            Формирование представления для добавления нового жанра
        """
        try:
            data = request.json
            genre_service.create_genre(data)
            return 'Жанр добавлен', 201
        except Exception as e:
            return f'{e}', 404


@genre_ns.route("/<int:gid>")
class GenreViews(Resource):
    @auth_required
    def get(self, gid: int):
        """
            Формирование представления для получения жанра по id
        """
        try:
            genre = genre_service.get_one_genre(gid)
            return genre_schema.dump(genre), 200
        except Exception:
            return 'Таких жанров нет'


    @admin_required
    def put(self, gid):
        """
            Формирование представления для изменения данных режиссера
        """
        try:
            data = request.json
            data["id"] = gid
            genre_service.update_genre(data)
            return 'Данные о жанре обновлен', 201
        except Exception as e:
            return f'{e}', 404

    @admin_required
    def delete(self, gid):
        """
            Формирование представления для удаления жанра по id
        """
        try:
            genre_service.delete_genre(gid)
            return 'Жанр удален', 201
        except Exception as e:
            return f'{e}', 404


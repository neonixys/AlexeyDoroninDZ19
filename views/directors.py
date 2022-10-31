# Импорт необходимых библиотек
from flask import request
from flask_restx import Resource, Namespace

# Импорт схемы Director
from dao.model.director import DirectorSchema
from decorators import auth_required, admin_required
# Импорт экземпляра класса DirectorService
from implemented import director_service

# Импорт декораторов

# Формирование нэймспейса
director_ns = Namespace('directors')

# Формирование сереилизаторов для модели Director для одного элемента и для списка
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        """
            Формирование представления для получения режиссеров
        """
        try:
            directors = director_service.get_all_directors()
            return directors_schema.dump(directors), 200
        except Exception:
            return 404

    @admin_required
    def post(self):
        """
            Формирование представления для добавления нового режиссера
        """
        try:
            data = request.json
            director_service.create_director(data)
            return 'Режиссер добавлен', 201
        except Exception as e:
            return f'{e}', 404


@director_ns.route("/<int:did>")
class DirectorView(Resource):
    @auth_required
    def get(self, did: int):
        """
            Формирование представления для получения режиссера по id
        """
        try:
            director = director_service.get_one_director(did)
            return director_schema.dump(director), 200
        except Exception:
            return 'Такого режиссера нет'


    @admin_required
    def put(self, did):
        """
            Формирование представления для изменения данных режиссера
        """
        try:
            data = request.json
            data["id"] = did
            director_service.update_director(data)
            return 'Данные о режиссере обновлены', 201
        except Exception as e:
            return f'{e}', 404


    @admin_required
    def delete(self, did):
        """
            Формирование представления для удаления режиссера по id
        """
        try:
            director_service.delete_director(did)
            return 'Данные о режиссере удалены', 201
        except Exception as e:
            return f'{e}', 404

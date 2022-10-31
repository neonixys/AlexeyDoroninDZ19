from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from decorators import admin_required, auth_required
from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MovieViews(Resource):
    @auth_required
    def get(self):
        director = request.args.get("director_id")

        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        all_movies = movie_service.get_all_movies(filters)
        res = movies_schema.dump(all_movies)
        return res, 200


    @admin_required
    def post(self):
        """
            Формирование представления для добавления нового режиссера
        """
        try:
            data = request.json
            movie_service.create_movie(data)
            return 'Данные внесены', 201
        except Exception as e:
            return f'{e}', 404


@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    @auth_required
    def get(self, mid: int):
        """
            Формирование представления для получения фильма по id
        """
        try:
            movie = movie_service.get_one_movie(mid)
            return movie_schema.dump(movie), 200
        except Exception:
            return 'Такого фильма нет'


    @admin_required
    def put(self, mid):
        try:
            data = request.json
            data["id"] = mid
            movie_service.update_movie(data)
            return 'Данные о фильме изменены', 201
        except Exception as e:
            return f'{e}', 404



    @admin_required
    def delete(self, mid: int):
        try:
            movie_service.delete_movie(mid)
            return 'Данные удалены', 201
        except Exception as e:
            return e, 404

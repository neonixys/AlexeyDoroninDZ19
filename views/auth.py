from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route("/")
class AuthViews(Resource):
    def post(self):
        data = request.json

        username = data.get('username', None)
        password = data.get('password', None)

        if None in [username, password]:
            return "Отсутствует логин или пароль", 400

        tokens = auth_service.generate_tokens(username, password)

        return tokens, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token')
        print(refresh_token)

        tokens = auth_service.approve_refresh_token(refresh_token)

        return tokens, 201

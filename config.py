from flask import app


class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_PRETTYPRINT_REGULAR = True
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}



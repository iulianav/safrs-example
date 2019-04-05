# flake8: noqa: F405
from .base import *  # noqa: F401,F403


DEBUG = True
TESTING = True

DB_NAME = 'safrs_test'
DB_USER = 'postgres'
DB_PWD = 'postgres'
SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}/{DB_NAME}'

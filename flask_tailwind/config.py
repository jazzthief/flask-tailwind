from os import path, environ
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# not using classes for now
DEBUG = True
TESTING = False
ENV = environ.get('FLASK_ENV')
SECRET_KEY = environ.get('SECRET_KEY')


""" class Config(object):
    DEBUG = False
    TESTING = False
    ENV = environ.get('FLASK_ENV')
    DATABASE_URI = 'sqlite:///:memory:'
    SECRET_KEY = environ.get('SECRET_KEY')


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True """

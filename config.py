import os
from os import path, environ
from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))

# Carregar as variáveis de ambiente do arquivo `.flaskenv`
# load_dotenv('.flaskenv')

class Config:

  # Default settings
  FLASK_ENV = 'development'
  DEBUG = False
  TESTING = False
  WTF_CSRF_ENABLED = True
  # SERVER_NAME = '06916f47-db6b-4d2e-a5b8-8ac30faff09d.id.repl.co'

  # Settings applicable to all environments
  SECRET_KEY = os.getenv('SECRET_KEY', default='chave_super_secreta.')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  PREFERRED_URL_SCHEME='https'


class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///database_dev.db'
  # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'database_dev.db')


class TestingConfig(Config):
  TESTING = True
  WTF_CSRF_ENABLED = False
  MAIL_SUPPRESS_SEND = True
  # SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'test.db')
  SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


class ProductionConfig(Config):
  FLASK_ENV = 'production'
  SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URI')
  # SQLALCHEMY_DATABASE_URI = os.getenv('JAWSDB_MARIA_URL',
  #                                     default="sqlite:///" +
  #                                     os.path.join(BASE_DIR, 'prod.db'))

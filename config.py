import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    STATIC_FOLDER = 'app/static'
    TEMPLATES_FOLDER = 'app/templates'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'mysql+mysqlconnector://user:password@db/microservices_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_KEY = os.environ.get('API_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    STATIC_URL = '/static/'

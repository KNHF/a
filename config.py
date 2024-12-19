import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key'
    STATIC_URL = '/static/'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_URL = '/static/'


class RandomNumberConfig(DevelopmentConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@db_random_number/random_number_db'


class EvenOddConfig(DevelopmentConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@db_even_odd/even_odd_db'


class ApiGatewayConfig(DevelopmentConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@db_api_gateway/api_gateway_db'

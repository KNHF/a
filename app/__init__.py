from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

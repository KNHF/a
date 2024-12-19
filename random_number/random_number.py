from flask import Flask, jsonify, render_template
from app.models import db, ExampleModel
from flask_migrate import Migrate
import config
import random


def create_app():
    app = Flask(__name__, template_folder='../app/templates',
                static_folder='../app/static')
    app.config.from_object(config.RandomNumberConfig)

    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route("/", methods=['GET'])
    def home():
        return render_template("index.html")

    @app.route("/generate", methods=['GET'])
    def generate_random_number():
        random_number = random.randint(1, 1000)
        return jsonify({"random_number": random_number})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=8001)

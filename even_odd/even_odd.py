from flask import Flask, jsonify, request
from app.models import db, ExampleModel
from flask_migrate import Migrate
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route("/check", methods=['POST'])
    def check_even_odd():
        number = request.json.get("number")
        if number % 2 == 0:
            return jsonify({"result": "even"})
        else:
            return jsonify({"result": "odd"})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=8002)

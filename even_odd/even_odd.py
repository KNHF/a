from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

# Initialize the database
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.EvenOddConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/check", methods=['POST'])
    def check_even_odd():
        data = request.get_json()
        if not data or 'number' not in data:
            return jsonify({"error": "Invalid input"}), 400

        number = data.get("number")
        if not isinstance(number, int):
            return jsonify({"error": "Invalid input type"}), 400

        if number % 2 == 0:
            return jsonify({"result": "even"}), 200
        else:
            return jsonify({"result": "odd"}), 200

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8002)

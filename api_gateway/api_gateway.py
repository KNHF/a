from app.views import main as main_blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register blueprints if any
app.register_blueprint(main_blueprint)

if __name__ == "__main__":
    app.run(port=8000, debug=True)

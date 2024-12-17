from flask import Flask


def create_app():
    app = Flask(__name__)

    # بارگذاری تنظیمات از config.DevelopmentConfig
    app.config.from_object("config.DevelopmentConfig")

    # وارد کردن و ثبت blueprints
    from app.views import main
    app.register_blueprint(main)

    return app

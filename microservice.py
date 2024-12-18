
from app import create_app
app = create_app()

# from flask import Flask, render_template

# app = Flask(__name__)


# @app.route("/", methods=['GET'])
# def home():
#    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)

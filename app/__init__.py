import os
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return render_template("initial/welcome.html")

    return app

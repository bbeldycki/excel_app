from flask import Flask, render_template
import os


def create_app():
    app = Flask(__name__)
    path = "app/static/filesuploaded"
    path1 = "app/static/col_rm_final"
    try:
        os.makedirs(path)
        os.makedirs(path1)
    except OSError:
        pass
    app.config['SECRET_KEY'] = 'argagathtrhwtrh'

    @app.route('/')
    def hello():
        return render_template("initial/welcome.html")

    from . import col_rm
    app.register_blueprint(col_rm.bp)

    return app

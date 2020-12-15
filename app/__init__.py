from flask import Flask, render_template
import os

path = "app/static/filesuploaded"
path1 = "app/static/col_rm_final"


def create_app():
    app = Flask(__name__)

    check_catalogs_exist(path)
    check_catalogs_exist(path1)

    app.config['SECRET_KEY'] = 'argagathtrhwtrh'

    @app.route('/')
    def hello():
        check_catalogs_empty(path)
        check_catalogs_empty(path1)
        return render_template("initial/welcome.html")

    from . import col_rm
    app.register_blueprint(col_rm.bp)

    return app


def check_catalogs_exist(check_path):
    try:
        os.makedirs(check_path)
    except OSError:
        pass


def check_catalogs_empty(check_path):
    dirs = os.listdir(check_path)
    for file in dirs:
        os.remove(check_path + '/' + file)

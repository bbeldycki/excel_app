from flask import Flask, render_template
import os


# my local paths
path = os.path.abspath("app/filesuploaded")
path1 = os.path.abspath("app/col_rm_final")
path2 = os.path.abspath("app/excelmerged")
# for my pythonanywhere paths
# path = "/home/Flippy9004/excel_app/app/static/filesuploaded"
# path1 = "/home/Flippy9004/excel_app/app/static/col_rm_final"
# path2 = "/home/Flippy9004/excel_app/app/static/excelmerged"


def create_app():
    app = Flask(__name__)

    check_catalogs_exist(path)
    check_catalogs_exist(path1)
    check_catalogs_exist(path2)

    app.config['SECRET_KEY'] = 'argagathtrhwtrh'

    @app.route('/')
    def hello():
        check_catalogs_empty(path)
        check_catalogs_empty(path1)
        check_catalogs_empty(path2)
        return render_template("initial/welcome.html")

    from . import col_rm
    app.register_blueprint(col_rm.bp)

    from . import excmerge
    app.register_blueprint(excmerge.bpp)

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

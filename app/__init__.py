from flask import Flask, render_template
from pathlib import Path
import os


def create_app():
    app = Flask(__name__)
    path = "app/static/filesuploaded"
    try:
        os.makedirs(path)
    except OSError:
        pass
    data_folder = Path(path)
    app.config['upload_catalog'] = data_folder
    app.config['SECRET_KEY'] = 'argagathtrhwtrh'
    print(app.config['upload_catalog'])

    @app.route('/')
    def hello():
        return render_template("initial/welcome.html")

    from . import col_rm
    app.register_blueprint(col_rm.bp)

    return app

from flask import Blueprint, request, flash, redirect, render_template
from werkzeug.utils import secure_filename
from pathlib import Path
import os

bp = Blueprint('colclear', __name__)

allowed_extensions = set(['txt', 'xlsx'])


def allowed_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


@bp.route('/clupload', methods=["GET", "POST"])
def clupload():
    if request.method == "POST":

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        filse = request.files['file']
        filse1 = request.files['file1']
        # if 'file[]' not in request.files:
        #    flash('No file part')
        #    return redirect(request.url)
        files = [filse, filse1]
        print(files)
        for file in files:
            if file.filename == '':
                flash('No file selected')
                return redirect(request.url)

        for file in files:
            if file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
                files.remove(file)

        filenames = []
        for file in files:
            if file and allowed_files(file.filename):
                filename = secure_filename(file.filename)
                filenames.append(filename)
                file.save(os.path.join(Path("app/static/filesuploaded"), filename))

        return render_template("col_rm/upload.html", filse=filenames)
    return render_template("col_rm/upload.html")

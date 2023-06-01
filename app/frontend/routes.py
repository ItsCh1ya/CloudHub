import os
import glob
from flask import render_template, request, session, abort
from app import app, cfg


@app.route('/')
def route_index():
    return render_template("index.html")


@app.route('/signup')
def route_signup():
    return render_template("signup.html")


@app.route('/dashboard', methods=['GET', 'POST'])
def route_dashboard():
    if 'user_id' not in session:
        return abort(403)

    user_id = session['user_id']

    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(cfg['DEFAULT']['users_files_path'], str(user_id), file.filename))

    root_path = cfg['DEFAULT']['users_files_path']
    user_path = os.path.join(root_path, str(user_id))
    list_of_files = filter(os.path.isfile, glob.glob(os.path.join(user_path, '*')))

    # Get list of files with size
    files_with_size = []
    for file_path in list_of_files:
        filename = os.path.split(file_path)[-1]
        file_size = round(os.stat(file_path).st_size / (1024 * 1024), 2)
        files_with_size.append((filename, file_size))

    return render_template("dashboard.html", files_with_size=files_with_size)

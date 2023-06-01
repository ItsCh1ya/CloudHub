from flask import request, session, jsonify, send_file
from app import app, cfg
from app.backend.core.utils import get_project_root
import os


@app.route('/api/send_file', methods=['POST'])
def api_send_file():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'})
    user_id = session['user_id']

    file = request.files['file']
    root_path = cfg['DEFAULT']['users_files_path']
    file.save(f"{root_path}/{user_id}/{file.filename}")

    return jsonify({'success': True})


@app.route('/api/get_files')
def api_get_files():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'}), 403
    user_id = session['user_id']

    root_path = cfg['DEFAULT']['users_files_path']
    user_path = os.path.join(root_path, str(user_id))
    return jsonify({"success": True, "files": os.listdir(user_path)})


@app.route('/api/receive_file/<file>')
def receive_file(file: str):
    if 'user_id' not in session:
        return jsonify({"success": False, 'message': 'Not logged in'}), 403
    user_id = session['user_id']

    project_root = get_project_root()
    root_path = cfg['DEFAULT']['users_files_path']
    user_path = os.path.join(root_path, str(user_id))
    return send_file(f"{project_root}/{user_path}/{file}"), 200

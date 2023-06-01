import os
from flask import request, jsonify, session

from app import app, cfg
from app.backend.core.db import register, login


@app.route('/api/register', methods=['POST'])
def api_register():
    try:
        user_id = register(request.json["name"], request.json["password"], request.json["email"])
        if user_id:
            os.mkdir(cfg['DEFAULT']['users_files_path'] + f"/{user_id}")
            session['user_id'] = user_id
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"success": False, "message": "Registration failed"}), 400


@app.route('/api/login', methods=['POST'])
def api_login():
    try:
        user = login(request.json["email"], request.json["password"])
        session['user_id'] = user[0]
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"success": False, "message": "Login failed"}), 403

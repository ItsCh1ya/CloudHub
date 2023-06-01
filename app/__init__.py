from flask import Flask
import configparser, os

from app.backend.core.db import con, cur

app = Flask(__name__)
app.secret_key = 'super secret key lol'
app.config['SESSION_TYPE'] = 'filesystem'

cfg = configparser.ConfigParser()
cfg.read('config.ini')

if not os.path.exists(cfg['DEFAULT']['users_files_path']):
   os.makedirs(cfg['DEFAULT']['users_files_path'])

from app import frontend
from app.backend import api
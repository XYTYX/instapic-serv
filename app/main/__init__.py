import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__, static_folder='../../instapic/build', static_url_path='/')

    config_name = os.getenv('ENV') or 'dev'
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    CORS(app)

    @app.route('/')
    def index():
        return app.send_static_file('index.html') 

    return app

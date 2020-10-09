import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from .config import config_by_name

db = SQLAlchemy()

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
flask_bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__, static_folder='../../instapic/build', static_url_path='/')
    app.url_map.strict_slashes = False

    config_name = os.getenv('ENV') or 'dev'
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    CORS(app)

    return app

from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.post_controller import api as post_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus (restx) web service'
          )

api.add_namespace(user_ns, path='/v1/user')
api.add_namespace(auth_ns, path='/v1/auth')
api.add_namespace(post_ns, path='/v1/post')

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# db = SQLAlchemy(app)

# from models import User

# @app.route('/add/')
# def webhook():
#     name = "ram"
#     email = "ram@ram.com"
#     u = User(id = id, nickname = name, email = email)
#     print("user created", u)
#     db.session.add(u)
#     db.session.commit()
#     return "user created"

# @app.route('/delete/')
# def delete():
#     u = User.query.get(i)
#     db.session.delete(u)
#     db.session.commit()
#     return "user deleted"

# if __name__ == '__main__':
#     app.run()
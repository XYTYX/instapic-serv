from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.post_controller import api as post_ns
from .main.controller.health_controller import api as health_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus (restx) web service'
          )

api.add_namespace(user_ns, path='/v1/user')
api.add_namespace(auth_ns, path='/v1/auth')
api.add_namespace(health_ns, path='/health')
api.add_namespace(post_ns, path='/v1/post')
from flask import current_app
from flask_restx import Resource
from ..util.dto import StaticHtml

api = StaticHtml.api

@api.route('/')
class Static(Resource):
    def get(self):
        current_app.send_static_file('index.html')
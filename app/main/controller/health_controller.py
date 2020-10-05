from flask import make_response
from flask_restx import Resource, Namespace

api = Namespace("/health", description="health check")

@api.route("/")
class HealthCheck(Resource):
    def get(self):
        headers = {"Content-Type": "application/json"}
        return make_response(
            'OK',
            200,
            headers
        )
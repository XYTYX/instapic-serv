from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class PostDto:
    api = Namespace('post', description='post related operations')
    image = api.model('image', {
        'path': fields.String(required=True, description='path for image')
    })
    post = api.model('post', {
        'text': fields.String(description='text for post'),
        'images': fields.List(fields.Nested(image)),
        'public_id': fields.String(required=True, description='public id of post')
    })
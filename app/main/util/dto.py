from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('v1/user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier'),
    })


class AuthDto:
    api = Namespace('v1/auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class PostDto:
    api = Namespace('v1/post', description='post related operations')
    image = api.model('image', {
        'full_src': fields.String(required=True, description='full source for image')
    })
    post = api.model('post', {
        'text': fields.String(description='text for post'),
        'images': fields.List(fields.Nested(image)),
        'public_id': fields.String(required=True, description='public id of post'),
        'created_on': fields.String(required=True, description='date post was created'),
        'user_public_id': fields.String(required=True, description='public id of user who created this post')
    })
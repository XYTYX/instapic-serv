from flask import request
from flask_restx import Resource
from ..util.dto import PostDto
from ..service.post_service import new_post, get_all_posts
from app.main.service.auth_helper import Auth
from app.main.util.decorator import token_required, admin_token_required

api = PostDto.api
_post = PostDto.post


@api.route('/')
class NewPost(Resource):
    @api.doc('creates a new post')
    @token_required
    @api.marshal_list_with(_post)
    def post(self):
        user, status = Auth.get_logged_in_user(request)
        return new_post(user_id=user['data']['user_id'], request=request)

    @api.doc('gets all posts')
    @token_required
    @api.marshal_list_with(_post, envelope='posts')
    def get(self):
        return get_all_posts();


@api.route('/<public_id>')
@api.param('public_id', 'The post identifier')
@api.response(404, 'User not found.')
class Post(Resource):
    @api.doc('views a single post')
    @token_required
    @api.marshal_with(_post)
    def get(self):
        post = get_post(public_id)
        if not user:
            api.abort(404)
        else:
            return user
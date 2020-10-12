from flask import request
from flask_restx import Resource
from ..util.dto import PostDto
from ..service.post_service import new_post, get_all_posts, get_post, get_all_by_user
from app.main.service.auth_helper import Auth
from app.main.util.decorator import token_required, admin_token_required

api = PostDto.api
_post = PostDto.post


@api.route('/')
class NewPost(Resource):
    @api.doc('creates a new post')
    @token_required
    @api.marshal_with(_post)
    def post(self):
        user, status = Auth.get_logged_in_user(request)
        return new_post(public_id=user['data']['public_id'], request=request)

    @api.doc('gets all posts')
    @token_required
    @api.marshal_list_with(_post)
    def get(self):
        sort_by = request.args.get('sort_by')
        offset = request.args.get('offset')
        limit = request.args.get('limit')
        posts = get_all_posts(sort_by, offset, limit);
        return posts

#
@api.route('/<user_public_id>')
@api.param('user_public_id', 'The user identifier')
class GetPostByUser(Resource):
    @api.doc('gets all posts by a single user')
    @token_required
    @api.marshal_list_with(_post)
    def get(self, user_public_id):
        return get_all_by_user(user_public_id)


@api.route('/<public_id>')
@api.param('public_id', 'The post identifier')
class Post(Resource):
    @api.doc('gets a single post')
    @token_required
    @api.marshal_with(_post)
    def get(self, public_id):
        post = get_post(public_id)
        if not post:
            api.abort(404)
        else:
            return post
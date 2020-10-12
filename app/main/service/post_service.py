import uuid
import os
import datetime
from app.main.model.models import save_changes, Post, Image
from .upload_helper import upload_file_to_s3

def new_post(public_id, request):
    if 'file' not in request.files:
        response_object = {
            'status': 'fail',
            'message': 'No file part'
        }
        return response_object, 400

    file = request.files['file']

    if file.filename == '':
        response_object = {
            'status': 'fail',
            'message': 'No selected file'
        }
        return response_object, 400

    if file and allowed_file(file.filename):
        unique_filename = str(uuid.uuid4())

        form = request.form

        new_post = Post(
            user_public_id=public_id,
            created_on=datetime.datetime.utcnow(),
            text=form['text'],
            public_id=str(uuid.uuid4())
        )

        post_id = save_changes(new_post).id

        full_src = upload_file_to_s3(file, unique_filename)

        new_image = Image(
            post_id=post_id,
            created_on=datetime.datetime.utcnow(),
            filename=unique_filename,
            full_src=full_src
        )

        save_changes(new_image)
        return new_post

def get_post(public_id):
    return Post.query.filter_by(public_id=public_id).first()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def get_all_posts(sort_by):
    if (sort_by == 'by_users'):
        return Post.query.order_by(Post.user_public_id.desc()).all()
    else:
        return Post.query.order_by(Post.id.desc()).all()

def get_all_by_user(user_public_id):
    return Post.query.filter_by(user_public_id=user_public_id).order_by(Post.id.desc()).all()
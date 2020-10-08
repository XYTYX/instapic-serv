import uuid
import os
import datetime
from flask import current_app
from app.main.model.models import save_changes, Post, Image
from .upload_helper import upload_file_to_s3

def new_post(user_id, request):
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
        filename = str(uuid.uuid4())

        form = request.form

        new_post = Post(
            user_id=user_id,
            created_on=datetime.datetime.utcnow(),
            text=form['text'],
            public_id=str(uuid.uuid4())
        )

        post_id = save_changes(new_post).id

        new_image = Image(
            post_id=post_id,
            created_on=datetime.datetime.utcnow(),
            path=filename
        )

        save_changes(new_image)

        upload_file_to_s3(file, filename)        

        return new_post

def get_post(public_id):
    return Post.query.filter_by(public_id=public_id).first()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_all_posts(sort_by):
    if (sort_by == 'most_recent'):
        return Post.query.order_by(Post.id.desc()).all()
        
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
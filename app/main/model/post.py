from .. import db

class Post(db.Model):
    """ Model for representing posts """
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

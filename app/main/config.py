import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
    AWS_KEY = os.environ.get("AWS_INSTAPIC_ACCESS_KEY")
    AWS_SECRET = os.environ.get("AWS_INSTAPIC_SECRET_ACCESS_KEY")
    S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
    SECRET_KEY = os.urandom(32)


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
    AWS_KEY = os.environ.get("AWS_INSTAPIC_ACCESS_KEY")
    AWS_SECRET = os.environ.get("AWS_INSTAPIC_SECRET_ACCESS_KEY")
    S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
    SECRET_KEY = os.urandom(32)


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATA_URI = os.environ['DATABASE_URL']
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
    AWS_KEY = os.environ.get("AWS_INSTAPIC_ACCESS_KEY")
    AWS_SECRET = os.environ.get("AWS_INSTAPIC_SECRET_ACCESS_KEY")
    S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
    SECRET_KEY = os.urandom(32)


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY

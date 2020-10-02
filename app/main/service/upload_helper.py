import boto3, botocore
from config import S3_KEY, S3_SECRET, S3_BUCKET
from manage import app

s3 = boto3.client(
   "s3",
   aws_access_key_id=app.config['S3_KEY'],
   aws_secret_access_key=app.config['S3_SECRET']
)
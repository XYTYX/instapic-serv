import boto3
from flask import current_app

def upload_file_to_s3(file, filename, acl="public-read"):
    s3 = boto3.client(
            "s3",
            aws_access_key_id=current_app.config['AWS_KEY'],
            aws_secret_access_key=current_app.config['AWS_SECRET']
        )

    bucket_name = current_app.config['S3_BUCKET']

    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            filename,
            ExtraArgs={
                "ACL": acl
            }
        )

    except Exception as e:
        # boto3 doesn't currently support mocking the upload_fileobj function, so we can't
        # mock it yet
        if current_app.config['TESTING']:
            return ""
        print("An error occurred when trying to upload to S3: ", e)
        return e

    return "{}{}".format(current_app.config["S3_LOCATION"], filename)

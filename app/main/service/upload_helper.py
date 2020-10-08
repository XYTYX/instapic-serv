import boto3, botocore
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
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e

    return "{}{}".format(current_app.config["S3_LOCATION"], file.filename)

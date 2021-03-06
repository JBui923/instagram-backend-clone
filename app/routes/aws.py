import os
import boto3
from random import randrange
from flask import Blueprint, request
from ..models import db
from ..models.users import User
from ..models.posts import Post
from botocore.exceptions import ClientError
import logging

bp = Blueprint("aws", __name__, url_prefix="/api/aws")

UPLOAD_FOLDER = "uploads"
BUCKET = "appacademy-instagram-clone"


@bp.route("/upload/<object_name>")
def upload(object_name, bucket_name=BUCKET, fields=None, conditions=None, expiration=6000):
    s3_client = boto3.client('s3')

    file_name, mime_type = object_name.split(".")
    object_name = f"uploads/{randrange(10000)}{file_name}.{mime_type}"
    response = s3_client.generate_presigned_post(bucket_name, object_name, Fields=fields, Conditions=conditions, ExpiresIn=expiration)
    response["fileUrl"] = f"https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/{object_name}"
    return response

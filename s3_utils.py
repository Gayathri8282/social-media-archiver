import os
import requests
import boto3
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)


def download_image(image_url):
    response = requests.get(image_url, timeout=10)
    response.raise_for_status()
    return BytesIO(response.content)


def upload_image_to_s3(image_bytes, s3_key):
    s3_client.upload_fileobj(
        image_bytes,
        S3_BUCKET_NAME,
        s3_key,
        ExtraArgs={"ContentType": "image/jpeg"}
    )

    return f"https://{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{s3_key}"


if __name__ == "__main__":
    test_url = "https://picsum.photos/600/600"
    image = download_image(test_url)

    s3_path = upload_image_to_s3(
        image,
        "test/sample_image.jpg"
    )

    print("Uploaded to:", s3_path)

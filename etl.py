from youtube_client import fetch_recent_videos
from s3_utils import download_image, upload_image_to_s3
from sentiment import analyze_sentiment
from db import insert_post
from datetime import datetime


def run_pipeline():
    posts = fetch_recent_videos(query="machine learning", max_results=3)

    for post in posts:
        print(f"Processing YouTube video: {post['post_id']}")

        # 1. Download thumbnail
        image_bytes = download_image(post["image_url"])

        # 2. Upload thumbnail to S3
        s3_key = f"youtube/{post['post_id']}.jpg"
        s3_url = upload_image_to_s3(image_bytes, s3_key)

        # 3. Sentiment analysis
        sentiment = analyze_sentiment(post["caption"])

        # 4. Convert ISO timestamp → unix
        created_at_unix = int(
            datetime.fromisoformat(
                post["created_at"].replace("Z", "")
            ).timestamp()
        )

        # 5. Prepare DB record
        db_record = {
            "platform": "youtube",
            "post_id": post["post_id"],
            "author": post["author"],
            "caption": post["caption"],
            "sentiment": sentiment,
            "image_s3_url": s3_url,
            "like_count": post["like_count"],
            "created_at": created_at_unix
        }

        # 6. Insert into DB
        insert_post(db_record)

        print(f"Stored video {post['post_id']} successfully\n")


if __name__ == "__main__":
    run_pipeline()

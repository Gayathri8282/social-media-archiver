import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def get_db_connection():
    return psycopg2.connect(DATABASE_URL)


def insert_post(post):
    query = """
    INSERT INTO social_posts (
        platform,
        post_id,
        author_username,
        caption,
        sentiment,
        image_s3_url,
        like_count,
        created_at
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, to_timestamp(%s))
    ON CONFLICT (post_id) DO NOTHING;
    """

    values = (
        post["platform"],
        post["post_id"],
        post["author"],
        post["caption"],
        post["sentiment"],
        post["image_s3_url"],
        post["like_count"],
        post["created_at"]
    )

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query, values)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    sample_post = {
        "platform": "instagram",
        "post_id": "test_db_001",
        "author": "test_user",
        "caption": "Testing database insertion",
        "sentiment": "positive",
        "image_s3_url": "https://example-bucket.s3.amazonaws.com/test.jpg",
        "like_count": 42,
        "created_at": 1700000000
    }

    insert_post(sample_post)
    print("Inserted test row into database")

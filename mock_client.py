import time

def fetch_recent_posts(limit=5):
    current_time = int(time.time())

    mock_posts = [
        {
            "post_id": "mock_001",
            "platform": "instagram",
            "author": "public_user_1",
            "caption": "Exploring AI and machine learning trends!",
            "image_url": "https://picsum.photos/600/600",
            "like_count": 120,
            "created_at": current_time
        },
        {
            "post_id": "mock_002",
            "platform": "twitter",
            "author": "public_user_2",
            "caption": "Cloud + data pipelines are underrated.",
            "image_url": "https://picsum.photos/600/601",
            "like_count": 89,
            "created_at": current_time
        },
        {
            "post_id": "mock_003",
            "platform": "instagram",
            "author": "public_user_3",
            "caption": "NLP is everywhere now.",
            "image_url": "https://picsum.photos/600/602",
            "like_count": 200,
            "created_at": current_time
        }
    ]

    return mock_posts[:limit]


if __name__ == "__main__":
    data = fetch_recent_posts()
    for post in data:
        print(post)

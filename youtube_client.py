import os
import requests
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
BASE_URL = "https://www.googleapis.com/youtube/v3/search"


def fetch_recent_videos(query="machine learning", max_results=5):
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "order": "date",
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()
    videos = []

    for item in data.get("items", []):
        snippet = item["snippet"]
        video_id = item["id"]["videoId"]

        videos.append({
            "platform": "youtube",
            "post_id": video_id,
            "author": snippet["channelTitle"],
            "caption": f"{snippet['title']} {snippet.get('description', '')}",
            "image_url": snippet["thumbnails"]["high"]["url"],
            "like_count": 0,  # fetched later if needed
            "created_at": snippet["publishedAt"]
        })

    return videos


if __name__ == "__main__":
    videos = fetch_recent_videos()
    for v in videos:
        print(v)

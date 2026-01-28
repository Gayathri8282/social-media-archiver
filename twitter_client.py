import os
import requests
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

BASE_URL = "https://api.twitter.com/2/tweets/search/recent"


def fetch_recent_tweets(query="AI", max_results=10):
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    params = {
        "query": query,
        "max_results": max_results,
        "tweet.fields": "created_at,public_metrics",
        "expansions": "author_id,attachments.media_keys",
        "media.fields": "url",
        "user.fields": "username"
    }

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"Twitter API error: {response.text}")

    return response.json()


if __name__ == "__main__":
    data = fetch_recent_tweets()
    print(data)

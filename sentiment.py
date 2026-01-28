from textblob import TextBlob


def analyze_sentiment(text):
    if not text or not text.strip():
        return "neutral"

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"


if __name__ == "__main__":
    samples = [
        "I love building data pipelines!",
        "This is the worst API experience ever.",
        "Just another normal day."
    ]

    for text in samples:
        print(text, "->", analyze_sentiment(text))

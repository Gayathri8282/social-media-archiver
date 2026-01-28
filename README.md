📌 Social Media Image & Metadata Archiving Pipeline
Overview

This project implements an automated ETL pipeline to archive public social media images and metadata. The pipeline fetches recent posts, stores images in cloud storage (AWS S3), enriches metadata using basic NLP sentiment analysis, and persists structured data in a PostgreSQL database.

The system is designed with scalability, fault tolerance, and real-world data engineering practices in mind.

🧱 Architecture
(Mock Social Media Source)
        |
        v
 Image Download  →  AWS S3 (Image Storage)
        |
        v
 NLP Sentiment Analysis
        |
        v
 PostgreSQL (Metadata Storage)

🛠️ Tech Stack

Python – ETL orchestration

AWS S3 – Cloud object storage for images

PostgreSQL (Neon) – Relational database for metadata

TextBlob – Lightweight NLP sentiment analysis

boto3 – AWS SDK

psycopg2 – PostgreSQL client

📌 Platform Choice & Data Source Justification

The initial design targeted Instagram and Twitter/X, as specified in the task requirements. However, during implementation, both platforms presented access limitations that impacted real-time ingestion of public content within the given timeline.

Twitter/X’s current API policy restricts read access to public posts behind paid credits, even for non-commercial and academic use. Despite successful authentication and token generation, read requests for public tweets returned credit-depleted responses, making live ingestion infeasible without paid access.

Instagram’s official APIs (Instagram Graph API and Basic Display API) require a Business or Creator account linked to a Facebook Page and only allow access to media owned by the authenticated account. They do not support ingestion of arbitrary public posts or hashtag-based discovery without extended approval workflows, which exceed the scope and timeline of this task.

To ensure uninterrupted development and demonstrate the full ETL pipeline design, a mock data source was initially implemented. This mock client simulated realistic social media post structures, including captions, image URLs, timestamps, and engagement metrics, allowing the pipeline to be validated end-to-end while remaining API-agnostic.

Subsequently, the pipeline was integrated with the YouTube Data API v3, which provides officially supported, free access to public social media content, including images (video thumbnails) and textual metadata (titles and descriptions). This allowed the system to operate on real, live data while preserving the same ingestion, storage, NLP enrichment, and scheduling logic.

The final implementation demonstrates a production-style, platform-agnostic ETL pipeline. The data ingestion layer can be swapped with Instagram or Twitter APIs once appropriate access is approved, without requiring changes to downstream components such as cloud storage, database schema, or orchestration.

🔄 Data Pipeline Flow

Fetch recent public post data (mocked source due to API constraints)

Download associated image URLs

Upload images to AWS S3 with structured keys

Perform sentiment analysis on captions

Store enriched metadata in PostgreSQL

Prevent duplicate entries using unique post IDs

🗄️ Database Schema
social_posts (
    id BIGSERIAL PRIMARY KEY,
    platform VARCHAR,
    post_id UNIQUE,
    author_username VARCHAR,
    caption TEXT,
    sentiment VARCHAR,
    image_s3_url TEXT,
    like_count INT,
    created_at TIMESTAMP,
    archived_at TIMESTAMP
)

⏱️ Scheduling

The pipeline is designed to be executed periodically using a cron job.

Example cron configuration (every 6 hours):

0 */6 * * * /usr/bin/python3 etl.py


This setup respects API rate limits and ensures incremental data ingestion.

⚠️ Data Source Note

Due to strict access limitations and credit restrictions on public social media APIs (e.g., Twitter/X, Reddit, Instagram), a mock data source was used to simulate real social media posts during development.

The pipeline is API-agnostic by design — the mock client can be replaced with any approved public API client without changing downstream logic.

🔐 Security & Ethics

All credentials are stored securely using environment variables

No private or restricted content is accessed

No personal user data is analyzed or deanonymized

The project is strictly non-commercial and academic

🚀 Future Improvements

Replace mock source with approved live APIs

Add Airflow / EventBridge for orchestration

Extend NLP with topic modeling or keyword extraction

Add monitoring and logging (CloudWatch)

✅ Conclusion

This project demonstrates a production-style data engineering pipeline combining cloud infrastructure, structured storage, and NLP enrichment. It reflects real-world considerations such as API limitations, scalability, and ethical data handling.
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv(
    "SUPADATA_API_KEY"
)

def fetch_transcript(video_url):
    endpoint = (
        "https://api.supadata.ai/v1/youtube/transcript"
    )
    headers = {
        "x-api-key": API_KEY
    }
    params = {
        "url": video_url
    }
    response = requests.get(
        endpoint,
        headers=headers,
        params=params
    )
    return response.json()

def save_file(data):
    os.makedirs(
        "research/youtube-transcripts",
        exist_ok=True
    )
    title = data.get(
        "title",
        "video"
    )
    filename = (
        title.replace(" ","_")
        + ".md"
    )
    path = (
        "research/youtube-transcripts/"
        + filename
    )
    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(
            str(data)
        )
    print(
        "Saved:",
        path
    )

if __name__ == "__main__":
    url = input(
        "YouTube URL: "
    )
    result = fetch_transcript(
        url
    )
    save_file(
        result
    )
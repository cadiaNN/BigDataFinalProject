# youtube_data/data_collection.py

import os
import json
from googleapiclient.discovery import build
from .config import YOUTUBE_API_KEY

def fetch_youtube_data(query, max_results=50):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    return response

def save_data(data, filename='mcdonalds_eco_packaging_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    query = "McDonald's Eco Packaging"
    youtube_data = fetch_youtube_data(query)
    save_data(youtube_data)
    print("Data fetched and saved to mcdonalds_eco_packaging_data.json")

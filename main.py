# main.py

from youtube_data.data_collection import fetch_youtube_data, save_data
from youtube_data.sentiment_analysis import analyze_sentiment
import json

if __name__ == "__main__":
    query = "McDonald's Eco Packaging"
    youtube_data = fetch_youtube_data(query)
    save_data(youtube_data)

    with open('mcdonalds_eco_packaging_data.json', 'r') as f:
        data = json.load(f)
    df = analyze_sentiment(data)
    df.to_csv('mcdonalds_eco_packaging_sentiment.csv', index=False)
    print("Sentiment analysis completed and saved to mcdonalds_eco_packaging_sentiment.csv")

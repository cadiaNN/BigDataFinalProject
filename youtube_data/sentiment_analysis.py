# youtube_data/sentiment_analysis.py

import json
import pandas as pd
from textblob import TextBlob

def analyze_sentiment(video_data):
    sentiments = []
    for item in video_data['items']:
        title = item['snippet']['title']
        description = item['snippet']['description']
        text = title + " " + description
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        sentiments.append({
            'title': title,
            'description': description,
            'sentiment': sentiment
        })
    return pd.DataFrame(sentiments)

if __name__ == "__main__":
    with open('mcdonalds_eco_packaging_data.json', 'r') as f:
        data = json.load(f)
    df = analyze_sentiment(data)
    df.to_csv('mcdonalds_eco_packaging_sentiment.csv', index=False)
    print("Sentiment analysis completed and saved to mcdonalds_eco_packaging_sentiment.csv")

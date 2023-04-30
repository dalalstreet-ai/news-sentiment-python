import requests

class NewsSentimentDataSDK:
    def __init__(self):
        self.base_url = 'https://b7ooir8kk9.execute-api.us-east-1.amazonaws.com/dev/news-sentiment-data'

    def fetch_sentiment_data(self, platform_token, stock_name, news_sources=None):
        if not platform_token:
            raise ValueError("platformToken is required.")

        if news_sources is None:
            news_sources = []

        payload = {
            "platformToken": platform_token,
            "stockName": stock_name,
            "newsSources": news_sources
        }

        try:
            response = requests.post(self.base_url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Error fetching sentiment data: {e}")

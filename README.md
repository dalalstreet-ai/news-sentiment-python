# Dalalstreet.ai - News Sentiment Data Python SDK

The News Sentiment Data SDK is a Python package that allows you to interact with the News Sentiment Data API. The SDK provides an easy-to-use interface for fetching news sentiment data related to specific stocks from the API.

## Installation

Install the package using pip:

```bash
pip install dalalstreet-news-sentiment==0.1.0
```

The SDK requires the `requests` library, which will be installed automatically as a dependency.

## Usage

Import the `NewsSentimentDataSDK` class from the package and create a new instance:

```python
from dalalstreet-news-sentiment.news_sentiment_data import NewsSentimentDataSDK

platform_token = "your-platform-token" # Replace with your actual platform token (mandatory)

newsSentimentData = NewsSentimentDataSDK()
```

Make sure to replace `"your-platform-token"` with your actual platform token.

To fetch sentiment data, call the `fetch_sentiment_data` method with the required parameters:

```python
stock_name = "AAPL"   # Replace with the stock symbol or name for which you want to fetch sentiment data (optional)
news_sources = ["source1", "source2"] # Replace with a list of news sources to filter the sentiment data (optional)

try:
    sentiment_data = sdk.fetch_sentiment_data(platform_token, stock_name, news_sources)
    print("Sentiment data:", sentiment_data)
except ValueError as e:
    print(f"Error: {e}")
```

## Parameters

The `fetch_sentiment_data` method accepts the following parameters:

- `platform_token` (mandatory, string): The platform token used for authentication.
- `stock_name` (optinal, string): The stock symbol or name for which you want to fetch sentiment data.
- `news_sources` (optional, list of strings): A list of news sources to filter the sentiment data. If not provided, all sources will be considered.

## License

This SDK is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

Make sure to customize the content according to your package name, repository URL, and other relevant information. You can also add more information on how to contribute, report issues, or any other details specific to your project.

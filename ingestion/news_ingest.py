import requests

class NewsIngestor:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/everything"

    def fetch_news(self, query):
        params = {
            "q": query,
            "apiKey": self.api_key
        }
        response = requests.get(self.base_url, params=params)
        articles = response.json().get("articles", [])
        return [article["title"] + ". " + (article["description"] or "") for article in articles]

from textblob import TextBlob

class SentimentAnalyzer:
    def __init__(self):
        pass

    def get_sentiment(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity  # Returns a value between -1 and 1

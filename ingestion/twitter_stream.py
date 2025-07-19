import tweepy
from queue import Queue

class TwitterIngestor:
    def __init__(self, bearer_token, keywords):
        self.bearer_token = bearer_token
        self.keywords = keywords
        self.tweet_queue = Queue()

    def start_stream(self):
        class MyStream(tweepy.StreamingClient):
            def on_tweet(inner_self, tweet):
                self.tweet_queue.put(tweet.text)

        stream = MyStream(self.bearer_token)
        for keyword in self.keywords:
            stream.add_rules(tweepy.StreamRule(keyword))
        stream.filter(tweet_fields=["created_at", "lang"])

    def get_tweet(self):
        return self.tweet_queue.get()

from ingestion.reddit_ingest import RedditIngestor
from ingestion.news_ingest import NewsIngestor
from nlp.sentiment_analyzer import SentimentAnalyzer
from nlp.entity_tagger import EntityTagger
from signal.signal_generator import SignalGenerator
from utils.config import CONFIG

if __name__ == "__main__":
    sentiment_model = SentimentAnalyzer()
    entity_tagger = EntityTagger()
    signal_gen = SignalGenerator()

    # Fetch Reddit posts
    reddit = RedditIngestor(
        CONFIG['reddit_client_id'],
        CONFIG['reddit_client_secret'],
        CONFIG['reddit_user_agent'],
        CONFIG['subreddits']
    )
    posts = reddit.fetch_posts()

    # Analyze and print results
    for post in posts:
        sentiment = sentiment_model.get_sentiment(post)
        tags = entity_tagger.tag_instruments(post)
        signal, score = signal_gen.generate_signal(sentiment)
        print(f"Text: {post[:80]}...\nTagged: {tags}\nSentiment: {sentiment:.2f} → Signal: {signal}\n")

import praw

class RedditIngestor:
    def __init__(self, client_id, client_secret, user_agent, subreddits):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        self.subreddits = subreddits

    def fetch_posts(self, limit=10):
        posts = []
        for subreddit in self.subreddits:
            for submission in self.reddit.subreddit(subreddit).hot(limit=limit):
                if not submission.stickied:
                    posts.append(submission.title + ". " + submission.selftext)
        return posts

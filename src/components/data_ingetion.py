import praw
import json
import os

class RedditDataIngestion:
    def __init__(self, client_id, client_secret, user_agent, username, password):
        """
        Initialize the Reddit API client.
        """
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            username=username,
            password=password
        )

    def fetch_subreddit_posts(self, subreddit_name, limit=10):
        """
        Fetch posts from a specific subreddit.

        Args:
            subreddit_name (str): Name of the subreddit to fetch posts from.
            limit (int): Number of posts to fetch.

        Returns:
            list: A list of posts with title, author, and content.
        """
        subreddit = self.reddit.subreddit(subreddit_name)
        posts = []

        for post in subreddit.hot(limit=limit):
            posts.append({
                "title": post.title,
                "author": post.author.name if post.author else None,
                "content": post.selftext,
                "url": post.url
            })

        return posts

    def save_posts_to_file(self, posts, file_path):
        """
        Save posts to a JSON file.

        Args:
            posts (list): List of posts to save.
            file_path (str): Path to the file where posts will be saved.
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            json.dump(posts, file, indent=4)

# Example usage (replace with your credentials):
if __name__ == "__main__":
    reddit_client = RedditDataIngestion(
        client_id="your_client_id",
        client_secret="your_client_secret",
        user_agent="your_user_agent",
        username="your_username",
        password="your_password"
    )

    subreddit_posts = reddit_client.fetch_subreddit_posts("learnpython", limit=5)
    reddit_client.save_posts_to_file(subreddit_posts, "data/reddit_posts.json")
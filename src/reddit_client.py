import praw
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT
from typing import List, Optional

from url_validity import is_valid_reddit_url

class RedditClient:
    def __init__(self, client_id, client_secret, user_agent):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.reddit = self.authenticate()

    # Authenticate with Reddit using credentials from config.py
    def authenticate(self) -> Optional[praw.Reddit]:
        try:
            # Create a Reddit instance with the provided credentials
            reddit = praw.Reddit(client_id=self.client_id,
                                 client_secret=self.client_secret,
                                 user_agent=self.user_agent)
            print("Successfully authenticated.")
            return reddit
        except praw.exceptions.PRAWException as e:
            print(f"Authentication failed: {e}")
            return None
        
    def fetch_comments(self, submission_url: str, limit: int = 5) -> List[str]:
        if not self.reddit:
            return []
        
        try:
            # Fetch the submission using the URL
            submission = self.reddit.submission(url=submission_url)
            submission.comments.replace_more(limit=0)

            # Get all comments and sort them by score in descending order
            comments = submission.comments.list()
            sorted_comments = sorted(comments, key=lambda comment: comment.score, reverse=True)

            # Get the top comments based on the limit
            top_comments = sorted_comments[:limit]

            # Print the top comments
            for i,v in enumerate(top_comments):
                print(f"Comment {i + 1}: {v.body}")
                print(f"Score: {v.score}")
                print('-' * 80)

        except Exception as e:
            print(f"Error fetching comments: {e}")
            return []
        

if __name__ == "__main__":
    # Create a RedditClient instance
    reddit_client = RedditClient(CLIENT_ID, CLIENT_SECRET, USER_AGENT)

    # Prompt the user to enter a Reddit post URL
    submission_url = input("Enter a Reddit post URL: ")

    # Validate the Reddit post URL
    if not is_valid_reddit_url(submission_url):
        print("Invalid Reddit URL. Please enter a valid Reddit post URL.")
    else:
        # Fetch and display comments if the URL is valid
        reddit_client.fetch_comments(submission_url)


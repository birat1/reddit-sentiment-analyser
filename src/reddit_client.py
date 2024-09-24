import praw
from url_validity import is_valid_reddit_url

from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT

class RedditClient:
    # Initialize the Reddit client with the provided credentials
    def __init__(self, client_id, client_secret, user_agent):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.reddit = self.authenticate()

    # Authenticate the Reddit client
    def authenticate(self):
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
        
    # Fetch comments from a Reddit post    
    def fetch_comments(self, submission_url, limit=20):
        if not self.reddit:
            print("Reddit authentication failed. Cannot fetch comments.")
            return []
        
        try:
            # Fetch the submission using the URL
            submission = self.reddit.submission(url=submission_url)
            submission.comments.replace_more(limit=0)

            # Get all comments and sort them by score in descending order
            comments = submission.comments.list()
            top_comments = sorted(comments, key=lambda comment: comment.score, reverse=True)[:limit]

            # Store the top comments in a list
            top_comments_list = []
            for comment in top_comments:
                # Check if the comment is not deleted or removed
                if comment.body not in ['[deleted]', '[removed]']:
                    top_comments_list.append({"body": comment.body,
                                              "author": comment.author if comment.author else "[deleted]"
                                            })
            
            return top_comments_list

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
        comments = reddit_client.fetch_comments(submission_url)

        for comment in comments:
            print(comment)
            print()
        

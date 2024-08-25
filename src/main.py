from reddit_client import RedditClient
from url_validity import is_valid_reddit_url
from preprocess_data import preprocess
from sentiment_analysis import combined_sentiment_analysis

from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT

def main():
    # Create a RedditClient instance
    reddit_client = RedditClient(CLIENT_ID, CLIENT_SECRET, USER_AGENT)

    # Prompt the user to enter a Reddit post URL
    submission_url = input("Enter a Reddit post URL: ")

    # Validate the Reddit post URL
    if not is_valid_reddit_url(submission_url):
        print("Invalid Reddit URL. Please enter a valid Reddit post URL.")
        return
    
    # Fetch comments from the Reddit post
    comments = reddit_client.fetch_comments(submission_url)

    # Preprocess the comments
    cleaned_comments = preprocess(comments)

    # Perform sentiment analysis on the comments
    results = combined_sentiment_analysis(cleaned_comments)

    # Print the results for each comment
    for result in results:
        print(result)
        print()


if __name__ == "__main__":
    main()

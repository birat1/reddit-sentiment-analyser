from flask import Flask, request, render_template
from reddit_client import RedditClient
from url_validity import is_valid_reddit_url
from preprocess_data import preprocess
from sentiment_analysis import combined_sentiment_analysis

from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT

# Initialize the Flask application
app = Flask(__name__)

# Create a RedditClient instance
reddit_client = RedditClient(CLIENT_ID, CLIENT_SECRET, USER_AGENT)

# Render the index.html template
@app.route("/")
def index():
    return render_template("index.html")

# Analyze the Reddit post comments
@app.route("/analyze", methods=["POST"])
def analyze():
    # Get the Reddit post URL from the form
    submission_url = request.form['url']

    # Validate the Reddit post URL
    if not is_valid_reddit_url(submission_url):
        return "Invalid Reddit URL. Please enter a valid Reddit post URL."
    
    # Fetch comments from the Reddit post  
    comments = reddit_client.fetch_comments(submission_url)

    # Preprocess the comments
    cleaned_comments = preprocess(comments)

    # Perform sentiment analysis on the comments
    results = combined_sentiment_analysis(cleaned_comments)

    # Render the results.html template with the analysis results
    return render_template("results.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

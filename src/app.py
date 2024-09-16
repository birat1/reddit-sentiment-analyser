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
    submission_url = request.form["url"]

    # Validate the Reddit post URL
    if not is_valid_reddit_url(submission_url):
        return "Invalid Reddit URL. Please enter a valid Reddit post URL."

    # Fetch comments from the Reddit post
    comments = reddit_client.fetch_comments(submission_url)

    # Preprocess the comments
    cleaned_comments = preprocess(comments)

    # Perform sentiment analysis on the comments
    results = combined_sentiment_analysis(cleaned_comments)

    positive_comments = sum(1 for result in results if result['Basic Transformer Label'] == 'positive')
    negative_comments = sum(1 for result in results if result['Basic Transformer Label'] == 'negative')
    neutral_comments = sum(1 for result in results if result['Basic Transformer Label'] == 'neutral')

    summary = {
        'positive_comments': positive_comments,
        'negative_comments': negative_comments,
        'neutral_comments': neutral_comments
    }

    # Render the results.html template with the analysis results
    return render_template("results.html", results=results, summary=summary)


# Render dummy results for testing purposes
# @app.route("/test-results")
# def test_results():
#     dummy_results = [
#         {
#             "Comment": "This is a test comment.",
#             "TextBlob Polarity": 0.1,
#             "TextBlob Subjectivity": 0.5,
#             "VADER Score": 0.2,
#             "Basic Transformer Label": "Positive",
#             "Basic Transformer Score": 0.9,
#             "Fine-Grained Label": "Neutral",
#             "Fine-Grained Score": 0.7,
#         },
#         {
#             "Comment": "Another test comment.",
#             "TextBlob Polarity": -0.2,
#             "TextBlob Subjectivity": 0.4,
#             "VADER Score": -0.1,
#             "Basic Transformer Label": "Negative",
#             "Basic Transformer Score": 0.8,
#             "Fine-Grained Label": "Negative",
#             "Fine-Grained Score": 0.6,
#         },
#     ]
#     return render_template("results.html", results=dummy_results)


if __name__ == "__main__":
    app.run(debug=True)

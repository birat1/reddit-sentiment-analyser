# Reddit Sentiment Analyzer

This project performs sentiment analysis on Reddit comments using multiple sentiment analysis models, including TextBlob, VADER, and a distilbert model from Hugging Face.

## Project Structure

```plaintext
reddit-sentiment-analyzer/
│
├── src/                        # Source code directory
│   ├── config.py               # Configuration file for environment variables
│   ├── preprocess_data.py      # Script for preprocessing the data
│   ├── reddit_client.py        # Script for initiating and fetching comments
│   ├── sentiment_analysis.py   # Script containing sentiment analysis models
│   └── url_validity.py         # Script for error handling reddit URLs
├── requirements.txt            # List of dependencies
└── README.md                   # Project documentation
```

## Prerequisites

- Python 3.7 or higher
- Virtual environment (venv)
- pip
- Reddit Developer Application

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/birat1/reddit-sentiment-analyzer.git
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3. **Install the required packages**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:

    - Create a `.env` file in the project and add the following:

        ```env
        CLIENT_ID=
        CLIENT_SECRET=
        USER_AGENT=
        ```

    - You can obtain your Reddit API credentials by creating an application at [Reddit Apps](https://www.reddit.com/prefs/apps/).

## Dependencies
- `praw` - For interacting with the Reddit API.
- `textblob` - For sentiment analysis.
- `vaderSentiment` - For sentiment analysis using VADER.
- `transformers` - For sentiment analysis using Hugging Face transformer models.
- `nltk` - Natural Language Toolkit for text processing.

## TODO

- [x] Allow the user to input reddit URL to analyze comments.
- [x] Perform error handling on URL entered to confirm it's a reddit URL.
- [x] Retrieve top upvoted comments.
- [x] Implement basic sentiments. e.g. positive, negative
- [x] Implement various different models of sentiment analysis.
- [ ] Implement fine-grained sentiments. e.g. joy, anger, sadness
- [ ] Implement data visualization.
- [ ] Create a website to handle data visualisation.
- [ ] Add support for user to choose post on website.
- [ ] Add abiltiy to change graphs for sentiment analysis.
- [ ] Multi-language support

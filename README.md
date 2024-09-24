# Reddit Sentiment Analyzer

This project performs sentiment analysis on Reddit comments using multiple sentiment analysis models, including TextBlob, VADER, and transformer models from Hugging Face.

## Project Structure

```plaintext
reddit-sentiment-analyzer/
│
├── src/                        # Source code directory
│   ├── app.py                  # Script to run the sentiment analysis (website version)
│   ├── config.py               # Configuration file for environment variables
│   ├── main.py                 # Script to run the sentiment analysis (console version)
│   ├── preprocess_data.py      # Script for preprocessing the data
│   ├── reddit_client.py        # Script for initiating and fetching comments
│   ├── sentiment_analysis.py   # Script containing sentiment analysis models
│   └── url_validity.py         # Script for error handling reddit URLs
├── requirements.txt            # List of dependencies
└── README.md                   # Project documentation
```

## Prerequisites

- Python 3.7 or higher
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


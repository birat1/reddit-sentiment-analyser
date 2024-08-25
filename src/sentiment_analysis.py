from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline
from typing import Any, Dict, List, Tuple

# Initialize sentiment analysis once
vader_analyzer = SentimentIntensityAnalyzer()
transformer_sentiment = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

# Analyze sentiment using TextBlob
def textblob_sentiment(comment: str) -> Tuple[float, float]:
    blob = TextBlob(comment)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

# Analyze sentiment using VADER
def vader_sentiment(comment: str) -> float:
    scores = vader_analyzer.polarity_scores(comment)
    return scores['compound']

# Analyze sentiment using a Hugging Face transformer model
def transformer_sentiment_analysis(comment: str) -> Tuple[str, float]:
    result = transformer_sentiment(comment)
    return result[0]['label'], result[0]['score']

# Combine all sentiment analysis methods
def combined_sentiment_analysis(comment: List[str]) -> List[Dict[str, Any]]:
    results = []

    # Iterate over each comment and perform sentiment analysis
    for comment in comments:
        textblob_polarity, textblob_subjectivity = textblob_sentiment(comment)
        vader_score = vader_sentiment(comment)
        transformer_label, transformer_score = transformer_sentiment_analysis(comment)

        # Append the results to a list
        results.append({
            "Comment": comment,
            "TextBlob Polarity": textblob_polarity,
            "TextBlob Subjectivity": textblob_subjectivity,
            "VADER Score": vader_score,
            "Transformer Label": transformer_label,
            "Transformer Score": transformer_score
        })

    return results

if __name__ == "__main__":
    # Sanmple list of comments to analyze
    comments = [
        "movie super messy sometimes stuff kinda happens man fun bit better editing cut scene make flow better would perfect pretty fun messy movie",
        "seen ill recommend manage expectation good nothing mind blowing",
        "pretty fun film overall got fair share laugh big prop emma corrin hugh jackman adding emotional weight",
        "vfx bad script bad dialogue horrendous pacing place action scene unreadable actor old role",
        "saw movie fucking rip movie fucking awesome"
    ]

    # Perform combined sentiment analysis on the list of comments
    results = combined_sentiment_analysis(comments)
    
    # Print the results for each comment
    for result in results:
        print(result)
        print()
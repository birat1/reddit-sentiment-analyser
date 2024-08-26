from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline

# Initialize VADER sentiment analyzer
vader_analyzer = SentimentIntensityAnalyzer()

# Initialize transformer sentiment analysis models
basic_sentiment_model = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
fine_grained_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Analyze sentiment using TextBlob
def textblob_sentiment(comment):
    blob = TextBlob(comment)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

# Analyze sentiment using VADER
def vader_sentiment(comment):
    scores = vader_analyzer.polarity_scores(comment)
    return scores['compound']

# Analyze sentiment using a basic transformer model
def basic_sentiment_analysis(comment):
    result = basic_sentiment_model(comment)
    return result[0]['label'], result[0]['score']

def fine_grained_sentiment_analysis(comment):
    result = fine_grained_model(comment)[0]
    return result['label'], result['score']

# Combine all sentiment analysis methods
def combined_sentiment_analysis(comments):
    results = []

    # Iterate over each comment and perform sentiment analysis
    for comment in comments:
        original_comment = comment["Original"]
        cleaned_comment = comment["Cleaned"]

        textblob_polarity, textblob_subjectivity = textblob_sentiment(cleaned_comment)
        vader_score = vader_sentiment(cleaned_comment)
        basic_label, basic_score = basic_sentiment_analysis(cleaned_comment)
        fine_grained_label, fine_grained_score = fine_grained_sentiment_analysis(cleaned_comment)

        # Append the results to a list
        results.append({
            "Comment": original_comment,
            "TextBlob Polarity": textblob_polarity,
            "TextBlob Subjectivity": textblob_subjectivity,
            "VADER Score": vader_score,
            "Basic Transformer Label": basic_label,
            "Basic Transformer Score": basic_score,
            "Fine-Grained Label": fine_grained_label,
            "Fine-Grained Score": fine_grained_score
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
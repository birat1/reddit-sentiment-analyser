import re
import ssl
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download the necessary NLTK data files
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Initialize the lammatizer and the set of stop words
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Clean the comment by removing URLs, special characters, stop words, and converting to lowercase
def clean_comment(comment):
    # Remove URLs, special characters, and convert to lowercase
    comment = re.sub(r"http\S+|www\S+|https\S+|@\S+|#\S+", " ", comment)
    comment = re.sub(r"[^\w\s]", "", comment)
    comment = comment.lower()

    # Tokenize the comment
    tokens = word_tokenize(comment)
    # Lemmatize the tokens and remove stop words
    cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

    return " ".join(cleaned_tokens)

# Preprocess a list of comments
def preprocess(comments):
    processed_comments = []

    for comment in comments:
        # Replace newline and carriage return characters with spaces
        author = comment["author"]
        comment = comment["body"].replace('\n', ' ').replace('\r', ' ')

        cleaned_comment = clean_comment(comment)
        processed_comments.append({
            "Original": comment,
            "Cleaned": cleaned_comment,
            "Author": author
        })

    return processed_comments

if __name__ == "__main__":
    comments = [
        {"body": "Movie is super messy, sometimes stuff just kinda happens, but man it's fun. A bit better editing, cut some scenes, and make it flow better and this would be perfect. As it is, it's a pretty fun if messy movie.", "author": "User1"},
        {"body": "I have seen it… I'll recommend to manage your expectations. It's good but nothing mind blowing", "author": "User2"},
        {"body": "Pretty fun film overall, got its fair share of laughs out of me. Big props to Emma Corrin and Hugh Jackman for adding some emotional weight to this.", "author": "User3"},
        {"body": "The VFX are bad, the script is bad, the dialogues are horrendous, the pacing is all over the place, action scenes are unreadable, and the actors are all too old for their role.", "author": "User4"},
        {"body": "Just saw it, that movie fucking rips. Movies are fucking awesome", "author": "User5"}
    ]

    cleaned_comments = preprocess(comments)

    for comment in cleaned_comments:
        print(comment)
        print()
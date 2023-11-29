from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import nltk

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()
text = "I love home"
sentiment_score = sia.polarity_scores(text)
print(sentiment_score)

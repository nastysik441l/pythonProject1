from textblob import TextBlob

text = "I love home"
blob = TextBlob(text)
sentiment = blob.sentiment
print(sentiment)

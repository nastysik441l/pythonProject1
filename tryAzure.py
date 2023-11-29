from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

apiKey = "e5e704924a3d473989afe52e8bcf61e8"
endPoint = "https://nastasiia11.cognitiveservices.azure.com/"

credential = AzureKeyCredential(apiKey)
libClient = TextAnalyticsClient(endPoint, credential)

docs=[
    {
        "id":"1","language":"en","text":"I love home"
    }
]
response=libClient.analyze_sentiment(docs)

i=0
for result in response:
    document=docs[i]
    print("Document text"+ document["text"])
    print(result.sentiment)
    print(result.confidence_scores)
    i= i+1
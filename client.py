import requests

url = "http://127.0.0.1:5000/predict_sentiment"

review = input("Enter a review: ")

data = {"review": review}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    sentiment = result.get("sentiment")
    print(f"Sentiment: {sentiment:.4f}")
else:
    print(f"Error: {response.text}")

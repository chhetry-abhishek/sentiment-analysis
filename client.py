import requests

# Define the URL of your Flask server
url = "http://127.0.0.1:5000/predict_sentiment"

# Accept user input for the review text
review = input("Enter a review: ")

# Create a dictionary with the review
data = {"review": review}

# Send the POST request
response = requests.post(url, json=data)

# Check the response and print the sentiment score
if response.status_code == 200:
    result = response.json()
    sentiment = result.get("sentiment")
    print(f"Sentiment: {sentiment:.4f}")
else:
    print(f"Error: {response.text}")

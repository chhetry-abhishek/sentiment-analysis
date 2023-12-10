from flask import Flask, render_template, request
from textblob import TextBlob


app = Flask(__name__)

def analyze_sentiment(text):
    
    analysis = TextBlob(text)
    
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route("/analyze", methods=["GET", "POST"])
def index():
    sentiment = None

    if request.method == "POST":
        text = request.form["text"]
        sentiment = analyze_sentiment(text)

    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
:
    app.run(debug=True)

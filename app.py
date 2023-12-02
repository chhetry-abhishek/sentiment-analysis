from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    review = request.form['review']
    # Perform sentiment analysis on the 'review' variable (use your existing code here)
    sentiment_score = perform_sentiment_analysis(review)
    return f'Sentiment: {sentiment_score}'

if __name__ == '__main__':
    app.run(debug=True)

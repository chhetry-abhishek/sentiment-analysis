# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Load the pre-trained sentiment analysis model
model = tf.keras.models.load_model('C:/Users/ab986/Desktop/sentiment_analysis_project/data/sentiment_model.h5')  # Replace 'sentiment_model_path' with the actual path to your model
tokenizer = Tokenizer()
tokenizer.word_index = {'i': 1, 'love': 2, 'this': 3, 'product': 4}  # Replace with your tokenization settings

# Function to predict sentiment
def predict_sentiment(review):
    sequence = tokenizer.texts_to_sequences([review])
    padded_sequence = pad_sequences(sequence, maxlen=100)
    padded_sequence = padded_sequence.reshape(1, -1)  # Reshape the padded_sequence
    sentiment = model.predict(padded_sequence)[0][0]
    return sentiment

# Test the model
sample_review = "I love this product!"
sentiment = predict_sentiment(sample_review)
print("Sentiment:", sentiment)

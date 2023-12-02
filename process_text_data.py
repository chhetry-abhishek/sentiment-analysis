# Import necessary libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Define the file path to your cleaned data
file_path = r'C:\Users\ab986\Desktop\sentiment_analysis_project\data\cleaned\cleaned_book.unlabeled'

# Open the file and read its content
with open(file_path, 'r', encoding='utf-8') as file:
    text_data = file.read()

# Define the maximum number of words to keep
max_num_words = 10000  # You can adjust this as needed

# Tokenize the text data
tokenizer = Tokenizer(num_words=max_num_words, oov_token='<OOV>')
tokenizer.fit_on_texts([text_data])

# Get the word index
word_index = tokenizer.word_index

# Convert the text to sequences
sequences = tokenizer.texts_to_sequences([text_data])

# Define the maximum sequence length
max_sequence_length = 1000  # You can adjust this as needed

# Pad sequences to a fixed length
padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, truncating='post', padding='post')

# Print the first padded sequence as an example
print("Padded Sequence Example:")
print(padded_sequences[0])

# You can continue with further processing of the padded_sequences as needed

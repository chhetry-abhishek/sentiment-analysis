import pickle
from tensorflow.keras.preprocessing.text import Tokenizer

# Path to your preprocessed text data file
data_path = 'data/cleaned/cleaned_book.unlabeled'

# Load your preprocessed text data
with open(data_path, 'r', encoding='utf-8') as file:
    text_data = file.readlines()

# Initialize a tokenizer
tokenizer = Tokenizer()

# Fit the tokenizer on your text data
tokenizer.fit_on_texts(text_data)

# Save the tokenizer to a file
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("Tokenizer saved as 'tokenizer.pickle'.")

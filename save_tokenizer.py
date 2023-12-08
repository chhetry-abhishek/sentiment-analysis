
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer

data_path = 'data/cleaned/cleaned_book.unlabeled'

with open(data_path, 'r', encoding='utf-8') as file:
    text_data = file.readlines()

tokenizer = Tokenizer()

tokenizer.fit_on_texts(text_data)

with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("Tokenizer saved as 'tokenizer.pickle'.")

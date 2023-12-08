

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

file_path = r'C:\Users\ab986\Desktop\sentiment_analysis_project\data\cleaned\cleaned_book.unlabeled'

with open(file_path, 'r', encoding='utf-8') as file:
    text_data = file.read()

max_num_words = 10000  

tokenizer = Tokenizer(num_words=max_num_words, oov_token='<OOV>')
tokenizer.fit_on_texts([text_data])

word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences([text_data])

max_sequence_length = 1000 

padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, truncating='post', padding='post')

print("Padded Sequence Example:")
print(padded_sequences[0])


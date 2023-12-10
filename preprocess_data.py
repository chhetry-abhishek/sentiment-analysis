

import os
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

cleaned_data_path = 'C:\\Users\\ab986\\Desktop\\sentiment_analysis_project\\data\\cleaned' 
output_path = 'C:\\Users\\ab986\\Desktop\\sentiment_analysis_project\\data\\processed'  

if not os.path.exists(output_path):
    os.makedirs(output_path)

reviews = []
labels = []

def determine_label(filename):
    if 'positive' in filename:
        return 1
    elif 'negative' in filename:
        return 0
    else:
        return -1 

for filename in os.listdir(cleaned_data_path):
    label = determine_label(filename)
    if label != -1:  
        file_path = os.path.join(cleaned_data_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                review = line.strip()
                reviews.append(review)
                labels.append(label)

combined = list(zip(reviews, labels))
np.random.shuffle(combined)
shuffled_reviews, shuffled_labels = zip(*combined)

tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(shuffled_reviews)
sequences = tokenizer.texts_to_sequences(shuffled_reviews)

max_length = 100 
data = pad_sequences(sequences, maxlen=max_length, padding='post', truncating='post')

X_train, X_test, y_train, y_test = train_test_split(data, shuffled_labels, test_size=0.2, random_state=42)

np.save(os.path.join(output_path, 'X_train.npy'), X_train)
np.save(os.path.join(output_path, 'X_test.npy'), X_test)
np.save(os.path.join(output_path, 'y_train.npy'), y_train)
np.save(os.path.join(output_path, 'y_test.npy'), y_test)

import pickle
with open(os.path.join(output_path, 'tokenizer.pickle'), 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)


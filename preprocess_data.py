import os
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

# Define paths
cleaned_data_path = 'C:\\Users\\ab986\\Desktop\\sentiment_analysis_project\\data\\cleaned'  # Update with your path
output_path = 'C:\\Users\\ab986\\Desktop\\sentiment_analysis_project\\data\\processed'  # Update with your path

# Make sure the output directory exists
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Initialize lists for reviews and labels
reviews = []
labels = []

# Function to determine the label of a review
def determine_label(filename):
    if 'positive' in filename:
        return 1
    elif 'negative' in filename:
        return 0
    else:
        return -1  # for unlabeled or other types of reviews

# Read the cleaned data
for filename in os.listdir(cleaned_data_path):
    label = determine_label(filename)
    if label != -1:  # Only process labeled reviews
        file_path = os.path.join(cleaned_data_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                review = line.strip()
                reviews.append(review)
                labels.append(label)

# Shuffle the reviews and labels together
combined = list(zip(reviews, labels))
np.random.shuffle(combined)
shuffled_reviews, shuffled_labels = zip(*combined)

# Tokenize the text
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(shuffled_reviews)
sequences = tokenizer.texts_to_sequences(shuffled_reviews)

# Pad sequences
max_length = 100  # Adjust as needed based on review length
data = pad_sequences(sequences, maxlen=max_length, padding='post', truncating='post')

# Split the data
X_train, X_test, y_train, y_test = train_test_split(data, shuffled_labels, test_size=0.2, random_state=42)

# Save the processed data and labels
np.save(os.path.join(output_path, 'X_train.npy'), X_train)
np.save(os.path.join(output_path, 'X_test.npy'), X_test)
np.save(os.path.join(output_path, 'y_train.npy'), y_train)
np.save(os.path.join(output_path, 'y_test.npy'), y_test)

# Save the tokenizer for later use
import pickle
with open(os.path.join(output_path, 'tokenizer.pickle'), 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("Preprocessing complete. Files saved.")
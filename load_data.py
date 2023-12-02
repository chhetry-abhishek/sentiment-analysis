import numpy as np

def load_data(data_file):
    # Initialize lists to store reviews and labels
    reviews = []
    labels = []

    # Open the data file and read lines
    with open(data_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Split each line into review and label
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            review, label = parts
            reviews.append(review)
            labels.append(int(label))

    return reviews, labels

# Specify the path to your data file
data_file = 'path/to/your/data/file.txt'

# Load the data
reviews, labels = load_data(data_file)

# Convert labels to NumPy array
labels = np.array(labels)

# Print some sample data
for i in range(5):
    print(f"Review: {reviews[i]}, Label: {labels[i]}")
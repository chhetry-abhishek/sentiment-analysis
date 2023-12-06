import numpy as np

def load_data(data_file):
    reviews = []
    labels = []

    with open(data_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            review, label = parts
            reviews.append(review)
            labels.append(int(label))

    return reviews, labels

data_file = 'path/to/your/data/file.txt'

reviews, labels = load_data(data_file)

labels = np.array(labels)

for i in range(5):
    print(f"Review: {reviews[i]}, Label: {labels[i]}")
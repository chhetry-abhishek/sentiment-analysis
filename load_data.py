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

data_file = 'C:/Users/ab986/Desktop/sentiment_analysis_project/data/cleaned'

reviews, labels = load_data(data_file)

labels = np.array(labels)

for i in range(5):

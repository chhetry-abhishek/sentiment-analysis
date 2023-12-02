import os
import re
import random

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def clean_text(text):
    """Remove HTML tags and punctuations from the text."""
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuations
    text = text.lower()  # Convert to lowercase
    return text

def load_and_clean_reviews(directory, label_type):
    """Load and clean reviews from given directory."""
    reviews = []
    label = -1 if label_type == 'unlabeled' else (1 if label_type == 'positive' else 0)
    file_name = f'{label_type}.review'

    review_file = os.path.join(directory, file_name)
    if not os.path.exists(review_file):
        print(f"File not found: {review_file}")
        return reviews

    with open(review_file, 'r', encoding='utf-8') as file:
        for line in file:
            if '<review_text>' in line:
                review = clean_text(line)
                reviews.append((review, label))

    return reviews

def main():
    project_root = 'C:/Users/ab986/Desktop/sentiment-analysis'  # Update to your project root path
    data_dir = os.path.join(project_root, 'data/sorted_data_acl')
    output_dir = os.path.join(project_root, 'data')
    create_directory_if_not_exists(output_dir)

    categories = ['books', 'dvd', 'electronics', 'kitchen_&_housewares']
    all_reviews = []

    for category in categories:
        category_dir = os.path.join(data_dir, category)
        for label_type in ['positive', 'negative', 'unlabeled']:
            review_file = os.path.join(category_dir, f'{label_type}.review')
            if os.path.exists(review_file):
                all_reviews.extend(load_and_clean_reviews(category_dir, label_type))
            else:
                print(f"File not found: {review_file}")

    random.shuffle(all_reviews)
    split_index = int(len(all_reviews) * 0.8)

    train_data_file = os.path.join(output_dir, 'train_data.txt')
    test_data_file = os.path.join(output_dir, 'test_data.txt')

    with open(train_data_file, 'w', encoding='utf-8') as f:
        for review, label in all_reviews[:split_index]:
            f.write(f"{review}\t{label}\n")

    with open(test_data_file, 'w', encoding='utf-8') as f:
        for review, label in all_reviews[split_index:]:
            f.write(f"{review}\t{label}\n")

    print("Data preparation complete.")

if __name__ == "__main__":
    main()

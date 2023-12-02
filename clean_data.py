import os
import re

def clean_text(text):
    """Cleans the input text."""
    text = text.lower()  # convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    text = re.sub(r'\d+', '', text)  # remove numbers
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces
    return text

def clean_reviews(input_directory, output_directory):
    """Reads, cleans, and writes reviews to a new file."""
    # Check if the output directory exists, create it if it doesn't
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)
        # Make sure it's a file, not a directory
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                cleaned_reviews = [clean_text(line) for line in file]

            # Define the path for the cleaned data
            cleaned_file_path = os.path.join(output_directory, f'cleaned_{filename}')
            with open(cleaned_file_path, 'w', encoding='utf-8') as file:
                for review in cleaned_reviews:
                    file.write(f"{review}\n")

# Define your input and output directories
output_directory = r'C:\Users\ab986\Desktop\sentiment_analysis_project\data\cleaned'

# Clean the reviews
clean_reviews(input_directory, output_directory)
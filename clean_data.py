import os
import re

def clean_text(text):
    """Cleans the input text."""
    text = text.lower() 
    text = re.sub(r'[^\w\s]', '', text)  
    text = re.sub(r'\d+', '', text) 
    text = re.sub(r'\s+', ' ', text).strip()  
    return text

def clean_reviews(input_directory, output_directory):
    """Reads, cleans, and writes reviews to a new file."""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                cleaned_reviews = [clean_text(line) for line in file]

            cleaned_file_path = os.path.join(output_directory, f'cleaned_{filename}')
            with open(cleaned_file_path, 'w', encoding='utf-8') as file:
                for review in cleaned_reviews:
                    file.write(f"{review}\n")

output_directory = r'C:\Users\ab986\Desktop\sentiment_analysis_project\data\cleaned'

clean_reviews(input_directory, output_directory)
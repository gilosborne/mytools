import os
import pandas as pd
from translatepy import Translator
import spacy

# Load spaCy English model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    raise Exception("spaCy model not found. Please install it using 'python3 -m spacy download en_core_web_sm'.")

# Initialize Translator
translator = Translator()

# Define file path
file_path = "/Users/gilosbo/Documents/1Documents/*Personal/iOSdev/Grammarless/Translation/TranslationTable.xlsx"

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file '{file_path}' was not found.")

# Load the Excel file
df = pd.read_excel(file_path)

# Ensure columns are strings
df["Spanish"] = df["Spanish"].astype(str).replace({"nan": "", None: ""})
df["Category"] = df["Category"].astype(str).replace({"nan": "", None: ""})

# Map of spaCy POS abbreviations to full words
pos_map = {
    "PRON": "Pronoun",
    "ADP": "Adposition",
    "CCONJ": "Coordinating Conjunction",
    "PART": "Particle",
    "AUX": "Auxiliary",
    "SCONJ": "Subordinating Conjunction",
    "VERB": "Verb",
    "ADJ": "Adjective",
    "ADV": "Adverb",
    "NOUN": "Noun",
    "NUM": "Numeral",
    "INTJ": "Interjection",
    "PROPN": "Proper Noun",
    "X": ""
}

# Function to translate English to Spanish
def translate_to_spanish(word):
    try:
        if not isinstance(word, str) or not word.strip():
            return ""
        translation = translator.translate(word, "es")
        return translation.result
    except Exception as e:
        print(f"Error translating '{word}': {e}")
        return ""

# Function to classify parts of speech using spaCy
def classify_pos(word):
    try:
        if not isinstance(word, str) or not word.strip():
            return ""
        doc = nlp(word)
        pos_abbreviation = doc[0].pos_ if doc else ""
        return pos_map.get(pos_abbreviation, pos_abbreviation)  # Convert to full word
    except Exception as e:
        print(f"Error classifying '{word}': {e}")
        return ""

# Process the DataFrame efficiently with progress tracking
def process_rows(df):
    total_rows = len(df)
    spanish_updates = []
    category_updates = []

    for index, row in df.iterrows():
        english_word = row["English"]

        # Translate to Spanish if the "Spanish" column is blank
        if not row["Spanish"].strip():
            translated_word = translate_to_spanish(english_word)
            spanish_updates.append((index, translated_word))

        # Classify part of speech if the "Category" column is blank
        if not row["Category"].strip():
            pos_category = classify_pos(english_word)
            category_updates.append((index, pos_category))

        # Print progress every 100 rows
        if (index + 1) % 100 == 0 or index + 1 == total_rows:
            percent_complete = ((index + 1) / total_rows) * 100
            print(f"Progress: {percent_complete:.2f}% complete")

    # Update DataFrame in bulk
    for index, translated_word in spanish_updates:
        df.at[index, "Spanish"] = translated_word

    for index, pos_category in category_updates:
        df.at[index, "Category"] = pos_category

process_rows(df)

# Save the updated DataFrame to a new file
output_path = "/Users/gilosbo/Documents/1Documents/*Personal/iOSdev/Grammarless/Translation/TranslationTable-updated.xlsx"
df.to_excel(output_path, index=False)

print(f"Updated translation table saved to '{output_path}'.")

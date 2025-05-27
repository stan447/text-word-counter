# text-word-counter
The link to the web
https://text-word-counter-fnz5ptynkyocscoiqzzamg.streamlit.app/#word-frequency-analyzer-map-reduce-style

# 📘 Word Frequency Analyzer (MapReduce Style)

A Streamlit web application that analyzes text files and displays the most frequent words using a MapReduce-like approach, with stopword removal and visualization.

![App Screenshot](https://via.placeholder.com/800x500?text=Word+Frequency+Analyzer+Screenshot)

## Features

- **File Upload**: Accepts `.txt` files with multiple encoding support (UTF-8, Latin-1, CP1252, UTF-16)
- **MapReduce Simulation**: Processes text in chunks similar to Hadoop/MapReduce
- **Stopword Removal**: Filters out common English stopwords
- **Top 20 Words**: Displays a sorted table of most frequent words
- **Visualization**: Includes a bar chart of word frequencies
- **Encoding Detection**: Automatically handles different text encodings

## How to Use

1. **Upload a Text File**:
   - Click "Browse files" or drag-and-drop a `.txt` file
   - The app supports various text encodings automatically

2. **View Results**:
   - The app will display:
     - A table of the top 20 most frequent words
     - A bar chart visualization
   - Words are cleaned (punctuation removed) and stopwords filtered

3. **Example Files**:
   - Try with project Gutenberg texts, blog posts, or any substantial text document

## Requirements

- Python 3.7+
- Required packages (install via `pip install -r requirements.txt`):

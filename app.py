# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import nltk

nltk.download('stopwords')
stop_words = set(nltk.corpus.stopwords.words('english'))

st.set_page_config(page_title="Word Frequency Analyzer", layout="centered")

st.title("📘 Word Frequency Analyzer (MapReduce Style)")
st.write("Upload a `.txt` file. The app will remove common stopwords and show you the most frequent words.")

uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    
    # Simulate HDFS: Split into chunks by paragraph
    chunks = text.split('\n\n')
    
    # Map Step
    mapped = []
    for chunk in chunks:
        words = chunk.lower().split()
        mapped.extend([
            (word.strip(".,!?;:\"'()[]{}"), 1)
            for word in words
            if word.isalpha() and word not in stop_words
        ])
    
    # Reduce Step
    word_count = defaultdict(int)
    for word, count in mapped:
        word_count[word] += count
    
    # Convert to DataFrame and get top 20
    df = pd.DataFrame(word_count.items(), columns=["Word", "Count"])
    df = df.sort_values(by="Count", ascending=False).head(20)
    
    st.subheader("📊 Top 20 Words")
    st.dataframe(df.reset_index(drop=True))
    
    # Plot
    st.subheader("📈 Word Frequency Chart")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(df["Word"], df["Count"], color='cornflowerblue')
    plt.xticks(rotation=45)
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Top 20 Most Frequent Words")
    st.pyplot(fig)

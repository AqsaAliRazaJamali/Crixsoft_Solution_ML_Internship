import streamlit as st
from dataset import get_sample_articles
from model import summarize_article

st.set_page_config(page_title="News Article Summarizer ML", layout="wide")
st.title("📰 ML-Powered News Article Summarizer")
st.caption("Machine Learning Internship Task 3 — Crixsoft Solution")

# Load sample dataset
sample_df = get_sample_articles()

st.sidebar.header("Options & Samples")
use_sample = st.sidebar.checkbox("Use Sample News Article")

if use_sample:
    selected_title = st.sidebar.selectbox("Select Sample Article:", sample_df['title'].values)
    article_row = sample_df[sample_df['title'] == selected_title].iloc[0]
    default_text = article_row['article']
else:
    default_text = ""

article_input = st.text_area(
    "Paste News Article Text Here:",
    value=default_text,
    height=250,
    placeholder="Paste a long news article or press 'Use Sample News Article' in the sidebar..."
)

num_points = st.slider("Select Summary Length (Number of Key Sentences):", min_value=1, max_value=5, value=3)

if st.button("Generate Summary"):
    if not article_input.strip():
        st.warning("Please paste or select a news article to summarize.")
    else:
        summary_text, key_points = summarize_article(article_input, num_sentences=num_points)
        
        st.success("Summary Generated Successfully!")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📌 Key Points Summary")
            for idx, point in enumerate(key_points, 1):
                st.markdown(f"**{idx}.** {point}")
                
        with col2:
            st.subheader("📄 Paragraph Overview")
            st.info(summary_text)
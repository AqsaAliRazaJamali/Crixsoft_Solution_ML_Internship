import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    """Normalize whitespace and remove unwanted characters."""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def split_into_sentences(text):
    """Split article into clean sentences."""
    cleaned = clean_text(text)
    # Split by period, exclamation, or question mark
    sentences = re.split(r'(?<=[.!?]) +', cleaned)
    return [s.strip() for s in sentences if len(s.strip()) > 10]

def summarize_article(text, num_sentences=3):
    """
    Extractive Summarization Engine using TF-IDF & Cosine Similarity.
    Ranks sentences by central relevance across the document.
    """
    sentences = split_into_sentences(text)
    
    # Handle short inputs gracefully
    if len(sentences) <= num_sentences:
        return " ".join(sentences), sentences

    # 1. Feature Extraction: Vectorize sentences
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # 2. Compute pairwise similarity matrix across sentences
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # 3. Calculate sentence importance scores (sum of similarity weights)
    sentence_scores = similarity_matrix.sum(axis=1)

    # 4. Extract top N highest scoring sentence indices
    top_indices = np.argsort(sentence_scores)[-num_sentences:]
    
    # Sort indices chronologically to preserve narrative flow
    top_indices = sorted(top_indices)

    summary_sentences = [sentences[i] for i in top_indices]
    summary_text = " ".join(summary_sentences)
    
    return summary_text, summary_sentences

if __name__ == "__main__":
    test_article = (
        "Artificial Intelligence is rapidly revolutionizing the healthcare industry across the globe. "
        "Machine learning algorithms are now being utilized to detect diseases in medical imaging faster and with greater accuracy. "
        "Researchers are developing deep learning models that analyze X-rays to identify early signs of conditions like cancer. "
        "Furthermore, AI systems help hospital admin staff streamline operations and reduce diagnostic errors. "
        "By predicting patient risks, doctors can intervene early and personalize treatment plans."
    )
    summary, points = summarize_article(test_article, num_sentences=2)
    print("\n--- Article Summary ---")
    print(summary)
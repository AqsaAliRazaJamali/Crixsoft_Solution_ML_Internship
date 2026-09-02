# Task 03: Machine Learning News Article Summarizer

## 📌 Project Overview
An interactive **Extractive Text Summarization Engine** that automatically condenses long news articles into concise, key insights. The model evaluates sentence importance by vectorizing sentence contents using **TF-IDF Vectorization** and measuring document centrality using **Cosine Similarity matrices**.

---

## 🔬 Machine Learning & NLP Pipeline
1. **Sentence Tokenization & Normalization**: Cleaned raw article text and segmented text into distinct sentence units.
2. **Feature Vectorization (TF-IDF)**: Built TF-IDF matrices across all individual sentences to extract keyword weights while ignoring common English stop words.
3. **Graph-Based Sentence Scoring**: Calculated pairwise Cosine Similarity values to measure how strongly each sentence represents the article's core topic.
4. **Summary Reconstruction**: Ranked sentences by centrality scores and re-ordered top sentences chronologically to preserve context flow.
5. **Interactive UI**: Custom Streamlit application supporting both custom copy-pasted articles and pre-loaded sample news categories.

---

## 📁 File Structure

| File Name | Description |
| :--- | :--- |
| `app.py` | Streamlit web application dashboard |
| `dataset.py` | Sample news articles loader |
| `model.py` | TF-IDF sentence vectorizer and centrality ranking engine |
| `requirements.txt` | Dependencies specification file |

---

## ⚙️ How to Run Locally (Windows Command Prompt)

1. Navigate to the Task 03 directory:
   ```cmd
   cd Task_03_News_Article_Summarizer

# Task 02_b: Sentiment Analysis using NLP & Machine Learning

![Task Status](https://img.shields.io/badge/Task%2002-Completed-brightgreen?style=for-the-badge)
![Domain](https://img.shields.io/badge/Domain-NLP%20%26%20Classification-blue?style=for-the-badge)
![Classifier](https://img.shields.io/badge/Algorithm-Logistic%20Regression-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## 📌 Project Overview
An interactive **Sentiment Analysis Engine** that determines the emotional tone (Positive, Negative, or Neutral) behind bodies of text such as customer feedback, reviews, and social media posts.

---

## 🔬 Machine Learning Pipeline
1. **Text Preprocessing & Feature Extraction**: Extracted n-gram text features using **TF-IDF Vectorization** (`TfidfVectorizer`) while removing English stop words.
2. **Classification Model**: Trained a **Logistic Regression** classifier wrapped inside a Scikit-Learn `Pipeline`.
3. **Probability Scoring**: Evaluated output probability distribution across Positive, Neutral, and Negative classes.
4. **Interactive UI**: Built a real-time web application using Streamlit to accept custom user inputs and display sentiment scores.

---

## 📁 Repository File Structure

| File Name | Description |
| :--- | :--- |
| `app.py` | Streamlit web application dashboard |
| `dataset.py` | Review dataset loader and sample text generator |
| `model.py` | TF-IDF feature extraction and Logistic Regression pipeline |
| `requirements.txt` | Dependency configuration file |

---

## ▶️ How to Run

### 1. Navigate to the Project Directory

Open Windows Command Prompt and navigate to the Task 2 directory:

```cmd
cd Task_02_Music_Recommendation_System
```

### 2. Activate the Virtual Environment

```cmd
..\venv\Scripts\activate
```

### 3. Install Dependencies

```cmd
pip install -r requirements.txt
```

### 4. Start the Streamlit Application

```cmd
streamlit run app.py
```

The Streamlit application will open in your default web browser.

---                              

## 👩‍💻 Author

**Aqsa Jamali**

GitHub: https://github.com/AqsaAliRazaJamali


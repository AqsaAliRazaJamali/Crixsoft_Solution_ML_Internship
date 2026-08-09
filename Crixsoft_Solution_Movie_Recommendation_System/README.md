# Task 01: Machine Learning Movie Recommendation System

##  Project Overview
An interactive **Machine Learning Recommendation System** built using Content-Based Filtering. The model cleans unstructured text features (genres and overviews), vectorizes text data using **TF-IDF Vectorization**, and computes pairwise distance matrix metrics using **Cosine Similarity** to provide personalized recommendations across 4,800+ movies.

---

##  Machine Learning Pipeline & Architecture
1. **Data Preprocessing**: Extracted clean genre strings from JSON-encoded metadata and combined them with movie plot overviews.
2. **Text Vectorization (TF-IDF)**: Transformed raw textual features into high-dimensional numerical vectors while discounting common stop words.
3. **Similarity Calculation**: Computed Cosine Similarity ($\cos(\theta)$) matrix to determine spatial similarity angles between vector representations.
4. **Interactive Dashboard**: Built a dynamic UI using Streamlit to accept user choices and render recommendations instantly.

---

## 📁 Repository File Structure

| File Name | Description |
| :--- | :--- |
| `app.py` | Streamlit web application user interface |
| `dataset.py` | Data loader, cleaner, and JSON parsing logic |
| `recommender.py` | Machine Learning model execution script |
| `requirements.txt` | Python dependency configuration |

---

## ▶️ How to Run

### 1. Navigate to the Project Directory

Open Windows Command Prompt and navigate to the task directory:

```cmd
cd Task_01_Movie_Recommendation_System
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

## 🔬 Recommendation Process

### 1. Data Preprocessing

Movie metadata is cleaned and prepared for analysis. JSON-encoded genre information is extracted into readable genre strings and combined with movie plot overviews.

### 2. TF-IDF Vectorization

The combined textual information is converted into numerical vectors using **TF-IDF (Term Frequency–Inverse Document Frequency)**. This allows the machine learning pipeline to represent the textual characteristics of each movie numerically.

### 3. Cosine Similarity

The system calculates **Cosine Similarity** between movie vectors to determine how closely related two movies are based on their textual features.

### 4. Recommendation Generation

Movies are ranked according to their similarity scores, and the most similar movies are returned as recommendations.

### 5. Interactive Dashboard

The Streamlit interface allows users to select a movie and instantly view recommended movies based on the calculated similarity scores.

---

##  Machine Learning Concepts Demonstrated

- Content-Based Filtering
- Natural Language Processing
- Data Preprocessing
- Feature Engineering
- TF-IDF Vectorization
- Cosine Similarity
- Similarity Matrices
- Recommendation Systems
- Interactive Machine Learning Applications

---

##  Key Highlights

- Content-based movie recommendation engine
- Recommendations across 4,800+ movies
- TF-IDF-based text representation
- Cosine Similarity-based ranking
- Interactive Streamlit interface
- Modular Python project architecture
- Practical application of machine learning and NLP concepts

---

## 👩‍💻 Author

**Aqsa Jamali**

GitHub: https://github.com/AqsaAliRazaJamali

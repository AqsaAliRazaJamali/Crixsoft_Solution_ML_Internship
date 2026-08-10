# 🎵 Task 02: Machine Learning Music Recommendation System

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Recommendation%20System-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

An interactive **Machine Learning Music Recommendation System** that analyzes Spotify-style audio features such as **Tempo, Energy, Danceability, Valence, and Acousticness**. The system normalizes numerical features using `StandardScaler` and calculates **Cosine Similarity** to recommend songs with similar acoustic and musical characteristics.

---

## 📌 Project Overview

This project demonstrates the practical implementation of a **content-based music recommendation system** using numerical audio features.

The system analyzes the acoustic profile of songs and recommends tracks that are most similar to a user's selected favorite song. An interactive **Streamlit dashboard** allows users to select tracks and customize the number of recommendations.

---

## ✨ Features

-  **Audio-Based Recommendations:** Recommends songs based on their musical and acoustic characteristics.
-  **Multiple Audio Features:** Analyzes Tempo, Energy, Danceability, Valence, and Acousticness.
-  **Feature Scaling:** Uses `StandardScaler` to normalize numerical features before similarity calculation.
-  **Cosine Similarity:** Measures similarity between song feature vectors.
-  **Personalized Recommendations:** Suggests tracks with audio profiles similar to the selected song.
-  **Interactive Streamlit Dashboard:** Provides an easy-to-use interface for selecting songs and viewing recommendations.
-  **Custom Recommendation Count:** Allows users to customize the number of recommended tracks.

---

## 🛠️ Technologies Used

### Machine Learning & Data Processing

- Python 3
- Pandas
- Scikit-learn
- StandardScaler
- Cosine Similarity

### Application

- Streamlit

---

## 📂 Project Structure

```text
Task_02_Music_Recommendation_System/
│
├── app.py                  # Streamlit web application dashboard
├── dataset.py              # Audio feature dataset loader and mock data generator
├── recommender.py          # Feature scaling and recommendation algorithm
├── requirements.txt        # Python dependency configuration
└── README.md               # Project documentation
```

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

##  Machine Learning Pipeline

```text
Music Dataset
      │
      ▼
Audio Feature Extraction
      │
      ▼
Tempo + Energy + Danceability
+ Valence + Acousticness
      │
      ▼
Feature Scaling
(StandardScaler)
      │
      ▼
Normalized Feature Vectors
      │
      ▼
Cosine Similarity
      │
      ▼
Similarity Ranking
      │
      ▼
Music Recommendations
```

---

## 🔬 Recommendation Process

### 1. Audio Feature Extraction

The system uses quantitative audio characteristics to represent each song, including:

- **Tempo:** Speed of the song measured in BPM.
- **Energy:** Perceived intensity and activity of the track.
- **Danceability:** How suitable the track is for dancing.
- **Valence:** The musical positivity or mood of the track.
- **Acousticness:** The degree to which the track contains acoustic characteristics.

### 2. Feature Scaling

The numerical features have different ranges and scales. `StandardScaler` normalizes these features so that individual variables do not disproportionately influence the similarity calculation.

### 3. Cosine Similarity

After scaling, the system calculates **Cosine Similarity** between song feature vectors. Higher similarity indicates that two songs have more closely related audio characteristics.

### 4. Recommendation Generation

Songs are ranked according to their similarity to the selected track, and the most similar songs are returned as recommendations.

### 5. Interactive Dashboard

The Streamlit application allows users to select a track and specify how many recommendations they want to receive.

---

## 📊 Audio Features Used

| Feature | Description |
|---|---|
| **Tempo** | Track speed measured in beats per minute (BPM) |
| **Energy** | Perceived intensity and activity of a track |
| **Danceability** | How suitable a track is for dancing |
| **Valence** | Musical positivity or mood |
| **Acousticness** | Degree of acoustic characteristics in a track |

---

## 📚 Machine Learning Concepts Demonstrated

- Recommendation Systems
- Content-Based Filtering
- Feature Engineering
- Feature Scaling
- Standardization
- Cosine Similarity
- Similarity Matrices
- Numerical Data Processing
- Interactive Machine Learning Applications

---

## 🎯 Key Highlights

- Audio-feature-based music recommendations
- StandardScaler-based feature normalization
- Cosine Similarity-based recommendation ranking
- Interactive Streamlit dashboard
- Customizable recommendation count
- Modular Python project architecture
- Practical application of machine learning concepts

---

## 👩‍💻 Author

**Aqsa Jamali**

GitHub: https://github.com/AqsaAliRazaJamali


import streamlit as st
import pandas as pd
from dataset import get_music_data
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Music Recommendation ML", layout="wide")
st.title("🎵 ML-Powered Music Recommendation System")
st.caption("Machine Learning Internship Task 2 — Crixsoft Solution")

@st.cache_data
def load_and_process_music():
    df = get_music_data()
    feature_cols = ['danceability', 'energy', 'valence', 'tempo', 'acousticness']
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[feature_cols])
    similarity_matrix = cosine_similarity(scaled_features, scaled_features)
    return df, similarity_matrix

df, similarity_matrix = load_and_process_music()

selected_song = st.selectbox("Select a song you enjoy:", df['track_name'].values)
num_recommendations = st.slider("Number of recommendations:", min_value=2, max_value=5, value=3)

if st.button("Get Music Recommendations"):
    idx = df[df['track_name'] == selected_song].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations + 1]
    
    st.subheader(f"Tracks similar to '{selected_song}' based on Audio Features:")
    cols = st.columns(len(sim_scores))
    
    for rank, item in enumerate(sim_scores):
        song_idx = item[0]
        score = round(item[1], 3)
        title = df.iloc[song_idx]['track_name']
        artist = df.iloc[song_idx]['artist']
        genre = df.iloc[song_idx]['genre']
        
        with cols[rank]:
            st.markdown(f"### 🎧 {title}")
            st.write(f"**Artist:** {artist}")
            st.caption(f"**Genre:** {genre}")
            st.markdown(f"**Audio Similarity:** `{score}`")
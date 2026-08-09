import streamlit as st
import requests
from dataset import get_movie_data
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page configuration
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 AI Movie Recommendation Engine")

# Cache data loading & similarity matrix calculation for performance
@st.cache_data
def load_data_and_similarity():
    df = get_movie_data()
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['content'])
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return df, similarity_matrix

df, similarity_matrix = load_data_and_similarity()

# Movie selection dropdown
movie_list = df['title'].values
selected_movie = st.selectbox("Type or select a movie you like:", movie_list)

# Number of recommendations slider
num_recommendations = st.slider("How many recommendations?", min_value=3, max_value=10, value=5)

def recommend(movie_title, top_n):
    idx = df[df['title'] == movie_title].index[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n + 1]
    
    recommended_movies = []
    for i in sim_scores:
        movie_idx = i[0]
        recommended_movies.append({
            'title': df.iloc[movie_idx]['title'],
            'genres': df.iloc[movie_idx]['clean_genres'],
            'overview': df.iloc[movie_idx]['overview'],
            'score': round(i[1], 3)
        })
    return recommended_movies

# Recommendation Trigger
if st.button("Get Recommendations"):
    st.subheader(f"Movies similar to '{selected_movie}':")
    results = recommend(selected_movie, num_recommendations)
    
    # Display results in structured columns
    cols = st.columns(num_recommendations)
    for index, col in enumerate(cols):
        if index < len(results):
            rec = results[index]
            with col:
                st.markdown(f"### {rec['title']}")
                st.caption(f"**Genres:** {rec['genres']}")
                st.markdown(f"**Similarity Score:** `{rec['score']}`")
                with st.expander("Read Plot Summary"):
                    st.write(rec['overview'])
import pandas as pd
from dataset import get_music_data
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

def recommend_songs(song_name, top_n=3):
    df = get_music_data()
    
    if song_name not in df['track_name'].values:
        return f"Error: '{song_name}' not found in dataset."

    # Select numerical audio feature columns
    feature_cols = ['danceability', 'energy', 'valence', 'tempo', 'acousticness']
    
    # Standardize numerical features so high tempo values don't dominate 0-1 features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[feature_cols])

    # Compute Cosine Similarity Matrix based on audio profiles
    similarity_matrix = cosine_similarity(scaled_features, scaled_features)

    # Locate target track index
    idx = df[df['track_name'] == song_name].index[0]
    
    # Get pairwise similarity scores
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n + 1]

    # Format output
    song_indices = [i[0] for i in sim_scores]
    recommendations = df.iloc[song_indices][['track_name', 'artist', 'genre']].copy()
    recommendations['similarity_score'] = [round(score[1], 3) for score in sim_scores]
    return recommendations

if __name__ == "__main__":
    test_song = "Blinding Lights"
    print(f"\n--- Music Recommendations for '{test_song}' ---")
    print(recommend_songs(test_song, top_n=3))
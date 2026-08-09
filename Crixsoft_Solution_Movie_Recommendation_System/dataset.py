import pandas as pd
import os
import json

def parse_genres(genres_json):
    """Extract clean genre names from the raw JSON string."""
    try:
        genres_list = json.loads(genres_json)
        return " ".join([item['name'] for item in genres_list])
    except Exception:
        return ""

def get_movie_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'tmdb_5000_movies.csv')
    
    df = pd.read_csv(file_path)
    df = df[['title', 'genres', 'overview']].copy()
    
    # Fill missing values
    df['genres'] = df['genres'].fillna('[]')
    df['overview'] = df['overview'].fillna('')
    
    # Extract clean genre keywords from JSON
    df['clean_genres'] = df['genres'].apply(parse_genres)
    
    # Combine cleaned genres and plot overview into a single text feature
    df['content'] = df['clean_genres'] + " " + df['overview']
    return df

if __name__ == "__main__":
    df = get_movie_data()
    print(f"Loaded {len(df)} movies from CSV!")
    print(df[['title', 'clean_genres']].head())
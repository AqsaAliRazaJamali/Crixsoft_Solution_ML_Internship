import pandas as pd
import os

def get_music_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'spotify_tracks.csv')
    
    # Check if external CSV dataset exists
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        # High-quality mock dataset with key Spotify audio features
        data = {
            'track_id': [1, 2, 3, 4, 5, 6, 7, 8],
            'track_name': [
                'Blinding Lights', 
                'Shape of You', 
                'Someone Like You', 
                'Levitating', 
                'Bohemian Rhapsody', 
                'Hotel California', 
                'Starboy', 
                'As It Was'
            ],
            'artist': [
                'The Weeknd', 
                'Ed Sheeran', 
                'Adele', 
                'Dua Lipa', 
                'Queen', 
                'Eagles', 
                'The Weeknd', 
                'Harry Styles'
            ],
            'genre': [
                'Synthpop', 
                'Pop', 
                'Soul Pop', 
                'Nu-Disco Pop', 
                'Classic Rock', 
                'Soft Rock', 
                'R&B Synthpop', 
                'Indie Pop'
            ],
            'danceability': [0.514, 0.825, 0.559, 0.702, 0.414, 0.579, 0.678, 0.520],
            'energy': [0.730, 0.652, 0.330, 0.825, 0.404, 0.508, 0.588, 0.731],
            'valence': [0.334, 0.931, 0.285, 0.915, 0.224, 0.609, 0.486, 0.662],
            'tempo': [171.00, 95.98, 135.10, 103.03, 71.10, 147.18, 186.05, 173.93],
            'acousticness': [0.001, 0.581, 0.892, 0.008, 0.288, 0.005, 0.141, 0.342]
        }
        df = pd.DataFrame(data)
        
    return df

if __name__ == "__main__":
    df = get_music_data()
    print(f"Loaded {len(df)} tracks successfully!")
    print(df[['track_name', 'artist', 'genre']].head())
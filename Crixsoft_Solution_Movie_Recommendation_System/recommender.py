from dataset import get_movie_data
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_movies(movie_title, top_n=3):
    # 1. Load the dataset
    df = get_movie_data()
    
    # Check if the requested movie exists
    if movie_title not in df['title'].values:
        return f"Error: '{movie_title}' is not found in the dataset."

    # 2. Convert text descriptions into numerical vectors (TF-IDF)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['content'])

    # 3. Compute Cosine Similarity matrix between all movies
    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # 4. Find the index of the input movie
    idx = df[df['title'] == movie_title].index[0]

    # 5. Get pairwise similarity scores for all movies with the input movie
    sim_scores = list(enumerate(similarity_matrix[idx]))

    # 6. Sort movies based on similarity scores (descending)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 7. Get the indices of top N most similar movies (excluding the input movie itself)
    sim_scores = sim_scores[1:top_n + 1]
    movie_indices = [i[0] for i in sim_scores]

    # Return top recommendations with similarity scores
    recommendations = df.iloc[movie_indices][['title', 'genres']].copy()
    recommendations['similarity_score'] = [round(score[1], 3) for score in sim_scores]
    return recommendations

if __name__ == "__main__":
    test_movie = "Inception"
    print(f"\n--- Movies similar to '{test_movie}' ---")
    results = recommend_movies(test_movie, top_n=3)
    print(results)
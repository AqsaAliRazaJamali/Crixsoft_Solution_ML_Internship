import pandas as pd
from dataset import get_review_data
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

def build_sentiment_model():
    df = get_review_data()
    
    # Machine Learning Pipeline: TF-IDF Feature Extraction + Logistic Regression Classifier
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1, 2))),
        ('classifier', LogisticRegression(random_state=42))
    ])
    
    # Train the pipeline on sample review data
    pipeline.fit(df['text'], df['sentiment'])
    return pipeline

def predict_sentiment(text_input, pipeline=None):
    if pipeline is None:
        pipeline = build_sentiment_model()
        
    prediction = pipeline.predict([text_input])[0]
    probabilities = pipeline.predict_proba([text_input])[0]
    classes = pipeline.classes_
    
    prob_dict = {classes[i]: round(probabilities[i], 3) for i in range(len(classes))}
    return prediction, prob_dict

if __name__ == "__main__":
    test_text = "The service was super fast and the team was extremely helpful!"
    sentiment, probs = predict_sentiment(test_text)
    print(f"\nText: '{test_text}'")
    print(f"Predicted Sentiment: {sentiment}")
    print(f"Confidence Probabilities: {probs}")
import streamlit as st
from model import build_sentiment_model, predict_sentiment

st.set_page_config(page_title="Sentiment Analysis ML", layout="wide")
st.title("🎭 ML-Powered Sentiment Analysis Engine")
st.caption("Machine Learning Internship Task 2 — Crixsoft Solution")

@st.cache_resource
def load_pipeline():
    return build_sentiment_model()

pipeline = load_pipeline()

st.subheader("Analyze Text Sentiment")
user_input = st.text_area("Enter customer review, feedback, or social media post:", 
                          value="The delivery was incredibly fast and the product quality exceeded my expectations!")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter valid text to analyze.")
    else:
        prediction, confidence = predict_sentiment(user_input, pipeline)
        
        # Display results with dynamic styling
        st.markdown("### Prediction Result")
        if prediction == "Positive":
            st.success(f"**Predicted Sentiment:** Positive 😊")
        elif prediction == "Negative":
            st.error(f"**Predicted Sentiment:** Negative 😞")
        else:
            st.info(f"**Predicted Sentiment:** Neutral 😐")
            
        st.markdown("### Confidence Probabilities")
        col1, col2, col3 = st.columns(3)
        col1.metric("Positive", f"{confidence.get('Positive', 0.0) * 100:.1f}%")
        col2.metric("Neutral", f"{confidence.get('Neutral', 0.0) * 100:.1f}%")
        col3.metric("Negative", f"{confidence.get('Negative', 0.0) * 100:.1f}%")
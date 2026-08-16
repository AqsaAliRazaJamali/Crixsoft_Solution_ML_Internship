import pandas as pd
import os

def get_review_data():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'customer_reviews.csv')
    
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        # High-quality sample dataset representing feedback, reviews, and posts
        data = {
            'text': [
                'The product quality is absolutely amazing! I love using it every day.',
                'Extremely disappointed. Item arrived broken and customer support was unhelpful.',
                'The package arrived today on time. It works fine as expected.',
                'Outstanding service! Fast delivery and exceptional quality.',
                'Terrible experience. Total waste of money and horrible interface.',
                'The app is okay, has basic features but nothing special.',
                'Super fast shipping and great customer experience!',
                'Defective product, stopped working after two days. Do not buy!',
                'Neutral feedback. It fulfills the basic function adequately.',
                'Best purchase I have made this year! High performance and easy to use.'
            ],
            'sentiment': [
                'Positive',
                'Negative',
                'Neutral',
                'Positive',
                'Negative',
                'Neutral',
                'Positive',
                'Negative',
                'Neutral',
                'Positive'
            ]
        }
        df = pd.DataFrame(data)
        
    return df

if __name__ == "__main__":
    df = get_review_data()
    print(f"Loaded {len(df)} sample reviews successfully!")
    print(df.head())
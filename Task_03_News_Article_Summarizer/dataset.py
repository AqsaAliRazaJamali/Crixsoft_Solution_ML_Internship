import pandas as pd
import os

def get_sample_articles():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'news_articles.csv')
    
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        # Pre-loaded news articles for quick demonstration
        data = {
            'title': [
                'AI Transformations in Healthcare',
                'Global Energy Transition Acceleration'
            ],
            'category': ['Technology', 'Environment'],
            'article': [
                "Artificial Intelligence is rapidly revolutionizing the healthcare industry across the globe. Machine learning algorithms are now being utilized to detect diseases in medical imaging faster and with greater accuracy than traditional methods. Researchers are developing deep learning models that analyze X-rays, MRIs, and CT scans to identify early signs of conditions like cancer. Furthermore, AI systems help hospital admin staff streamline operations, schedule appointments, and reduce diagnostic errors. By predicting patient risks, doctors can intervene early and personalize treatment plans. As technology advances, ethical considerations regarding patient data privacy and algorithm bias must be carefully addressed to ensure safe deployment.",
                "The shift toward renewable energy sources is accelerating globally in response to rising climate concerns. Solar and wind energy power generation have reached record capacity numbers over the past year. Governments are introducing financial incentives and green policies to encourage clean tech adoption among industries. Meanwhile, advances in battery storage technology are solving key reliability challenges associated with intermittent power generation. Electric vehicle adoption is also booming, reducing reliance on fossil fuels in transportation. Despite economic challenges and supply chain disruptions, experts predict that renewable energy will dominate the global power grid within the next decade."
            ]
        }
        df = pd.DataFrame(data)
        
    return df

if __name__ == "__main__":
    df = get_sample_articles()
    print(f"Loaded {len(df)} sample news articles successfully!")
    print(df[['title', 'category']].head())
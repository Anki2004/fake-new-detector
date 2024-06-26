import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def train_model():
    df = pd.read_csv(r'database\data.csv')
    df['Headline'] = df['Headline'].fillna(' ')

    X = df['Headline']
    y = df['Label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df = 0.7)
    X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
    X_test_tfidf = tfidf_vectorizer.transform(X_test)


    lr_model = LogisticRegression(random_state=42)
    lr_model.fit(X_train_tfidf, y_train)

    y_pred = lr_model.predict(X_test_tfidf)
    print(classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10,7))
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title('Confusion Matrix')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.savefig('confusion_matrix.png')


    def predict_fake_news(text):
        text_tfidf = tfidf_vectorizer.transform([text])
        prediction = lr_model.predict(text_tfidf)
        probability = lr_model.predict_proba(text_tfidf)

        return prediction[0], probability[0][1]
    
    sample_text = "NTA reform panel to elicit views of parents, students"
    prediction, probability = predict_fake_news(sample_text)
    print(f"Prediction: {'Fake' if prediction == 1 else 'Real'}")
    print(f"Probability of the news being fake is: {probability: .2f}")

    if not os.path.exists('backend/models'):
        os.makedirs('backend/models')
    joblib.dump(lr_model, 'backend/models/fake_news_model.py')
    joblib.dump(tfidf_vectorizer, 'backend/models/tfidf_vectorizer.py')

if __name__ == "__main__":
    train_model()
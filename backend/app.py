from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

model_path = os.path.join(os.path.dirname(__file__), 'models','fake_new_model.joblib' )
vectorizer_path = os.path.join(os.path.dirname(__file__), 'models','tfidf_vectorizer.joblib')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

@app.route('/predict', methods = ['POST'])
def predict():
    data = request.json
    text = data['text']
    text_vectorizer = vectorizer.transform([text])
    prediction = model.predict(text_vectorizer)[0]
    probability = model.predict_proba(text_vectorizer)[0][1]

    return jsonify({
        'prediction': 'fake' if prediction == 1 else 'Real',
        'probability': float(probability)
    })

if __name__ == "__main__":
    app.run(debug=True)
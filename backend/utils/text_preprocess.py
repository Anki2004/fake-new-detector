import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenizer

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]','',text)

    tokens = word_tokenizer(text)

    stop_Words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_Words]

    processed_text = ' '.join(tokens)
    return processed_text

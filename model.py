import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

def train_model(texts, labels):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    model = LogisticRegression()
    model.fit(X, labels)
    joblib.dump(model, 'classifier/model.pkl')
    joblib.dump(vectorizer, 'classifier/vectorizer.pkl')

def predict(text):
    model = joblib.load('classifier/model.pkl')
    vectorizer = joblib.load('classifier/vectorizer.pkl')
    X = vectorizer.transform([text])
    return model.predict(X)[0]

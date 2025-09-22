import pandas as pd
from classifier.model import train_model
from classifier.preprocess import clean_text

data = pd.read_csv('data/support_logs.csv')
texts = data['text'].apply(clean_text)
labels = data['label']
train_model(texts, labels)

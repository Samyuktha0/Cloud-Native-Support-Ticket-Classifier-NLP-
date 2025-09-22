import re

def clean_text(text):
    text = re.sub(r'\W+', ' ', text)
    return text.lower().strip()

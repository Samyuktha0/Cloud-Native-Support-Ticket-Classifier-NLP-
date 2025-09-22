# Cloud-Native Support Ticket Classifier (NLP)

An NLP-powered Django REST API that classifies support tickets and routes them to the correct engineering team. Built for scalable customer success automation.

## Features
- TF-IDF or BERT-based text classification
- REST API for ticket submission and prediction
- PostgreSQL backend with Redis caching
- Continuous learning via feedback loop

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

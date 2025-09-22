from rest_framework.decorators import api_view
from rest_framework.response import Response
from classifier.model import predict
from classifier.preprocess import clean_text

@api_view(['POST'])
def predict_ticket(request):
    text = request.data.get('text', '')
    cleaned = clean_text(text)
    label = predict(cleaned)
    return Response({'label': label})

@api_view(['POST'])
def feedback(request):
    # Placeholder for feedback loop
    return Response({'status': 'Feedback received'})

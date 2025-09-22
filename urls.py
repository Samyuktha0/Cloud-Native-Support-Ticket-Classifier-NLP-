from django.urls import path
from api.views import predict_ticket, feedback

urlpatterns = [
    path('predict/', predict_ticket),
    path('feedback/', feedback),
]

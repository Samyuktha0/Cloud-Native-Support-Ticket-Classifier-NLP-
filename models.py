from django.db import models

class Ticket(models.Model):
    text = models.TextField()
    predicted_label = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

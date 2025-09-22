from rest_framework import serializers

class TicketSerializer(serializers.Serializer):
    text = serializers.CharField()

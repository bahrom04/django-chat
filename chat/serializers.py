from rest_framework import serializers
from chat import models


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = ("id", "title")

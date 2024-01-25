# chat/views.py
from django.shortcuts import render
from rest_framework import generics
from chat import models, serializers


class MessageListView(generics.ListAPIView):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageListSerializer


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

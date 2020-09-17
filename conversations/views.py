""" Conversation app views """

from django.shortcuts import render
from rest_framework import viewsets

from .models import (
    Conversation,
    Message,
    Thought
)

from .serializers import (
    ConversationSerializer,
    MessageSerializer,
    ThoughtSerializer
)

class ConversationViewSet(viewsets.ModelViewSet):
    """ Conversation viewset """

    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()

class MessageViewSet(viewsets.ModelViewSet):
    """ Message viewset """

    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class ThoughtViewSet(viewsets.ModelViewSet):
    """ Thought viewset """

    serializer_class = ThoughtSerializer
    queryset = Thought.objects.all()

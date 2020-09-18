""" Conversation app serializers """

from rest_framework import serializers
from .models import (
    Conversation,
    Message,
    Thought
)

class ThoughtSerializer(serializers.ModelSerializer):
    """ Thought serializer """

    class Meta:
        model = Thought
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    """ Message serializer """

    thoughts = ThoughtSerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'conversation', 'text', 'date_time_created', 'thoughts']

class ConversationSerializer(serializers.ModelSerializer):
    """ Conversation serializer """

    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'title', 'start_date', 'messages']
        # depth = 2
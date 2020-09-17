""" Conversation app models """

from django.db import models
from django.utils import timezone

class Conversation(models.Model):
    """ Conversation model """

    title = models.CharField(max_length=200)
    start_date = models.DateField(
        auto_now_add=True,
        auto_now=False
    )

class Message(models.Model):
    """ Message model """
    
    conversation = models.ForeignKey(
        Conversation,
        related_name="messages",
        on_delete=models.CASCADE
    )
    text = models.TextField()
    date_time_created = models.DateTimeField(default=timezone.now)

class Thought(models.Model):
    """ Thought model """

    message = models.ForeignKey(
        Message,
        related_name="thoughts",
        on_delete=models.CASCADE
    )
    text = models.TextField()
    date_time_created = models.DateTimeField(default=timezone.now)



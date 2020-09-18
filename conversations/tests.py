""" Conversation app tests """

from django.test import TestCase
from .models import Conversation, Message, Thought

class ConversationTestCase(TestCase):
    """
    Test ensures conversation
    object is created
    with start date.
    """

    def setUp(self):
        Conversation.objects.create(title="test title")

    def test_conversation_has_a_start_date(self):
        conversation = Conversation.objects.get(title="test title")
        self.assertIsNotNone(conversation.start_date)

class MessageTestCase(TestCase):
    """
    Test ensures message object
    is created properly with
    conversation object in foreign
    key field.
    """

    def setUp(self):
        conversation = Conversation.objects.create(title="test conversation")
        Message.objects.create(conversation=conversation, text="test message")
    
    def test_message_foreign_key(self):
        message = Message.objects.get(text="test message")
        self.assertIsNotNone(message.conversation)

class MessageDeleteTestCase(TestCase):
    """
    Test ensures message objects can
    be deleted but their conversation
    object will not be deleted.
    """

    def setUp(self):
        conversation = Conversation.objects.create(title="test conversation")
        Message.objects.create(conversation=conversation, text="test message")
    
    def test_delete_message(self):
        conversation = Conversation.objects.get(title="test conversation")
        message = Message.objects.get(text="test message")
        message.delete()
        self.assertRaises(message.DoesNotExist)
        self.assertIsNotNone(conversation)

class ThoughtDeleteTestCase(TestCase):
    """
    Test ensures message objects can
    be deleted and their thought
    objects will also be deleted (CASCADE),
    but the conversation object will not be deleted.
    """

    def setUp(self):
        conversation = Conversation.objects.create(title="test conversation")
        message = Message.objects.create(conversation=conversation, text="test message")
        Thought.objects.create(message=message, text="test thought")

    def test_cascading_on_delete(self):
        conversation = Conversation.objects.get(title="test conversation")
        message = Message.objects.get(text="test message")
        thought = Thought.objects.get(text="test thought")
        message.delete()
        self.assertRaises(message.DoesNotExist)
        self.assertRaises(thought.DoesNotExist)
        self.assertIsNotNone(conversation)
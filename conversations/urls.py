""" Conversation app endpoints """

from rest_framework import routers

from .views import (
    ConversationViewSet,
    MessageViewSet,
    ThoughtViewSet
)

router = routers.DefaultRouter()

router.register('conversations', ConversationViewSet, 'conversations')
router.register('messages', MessageViewSet, 'messages')
router.register('thoughts', ThoughtViewSet, 'thoughts')

urlpatterns = router.urls
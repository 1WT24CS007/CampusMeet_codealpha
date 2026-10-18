from django.urls import re_path
from . import consumers
from . import meeting_consumers


websocket_urlpatterns = [

    # Text chat
    re_path(
        r"ws/chat/(?P<user_id>\d+)/$",
        consumers.ChatConsumer.as_asgi()
    ),

    # Video meeting signaling
    re_path(
        r"ws/meeting/(?P<room_name>[-\w]+)/$",
        meeting_consumers.MeetingConsumer.as_asgi()
    ),
]
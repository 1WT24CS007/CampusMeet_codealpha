
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class MeetingConsumer(WebsocketConsumer):

    def connect(self):
        self.user = self.scope["user"]
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"meeting_{self.room_name}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        username = (
            self.user.username
            if self.user.is_authenticated
            else "Guest"
        )

        print("MEETING USER:", username)
        print("MEETING ROOM:", self.room_group_name)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "user_joined",
                "username": username,
                "sender_channel": self.channel_name,
            }
        )

    def disconnect(self, close_code):
        if hasattr(self, "room_group_name"):
            async_to_sync(self.channel_layer.group_discard)(
                self.room_group_name,
                self.channel_name
            )

    def receive(self, text_data):
        try:
            data = json.loads(text_data)
        except (json.JSONDecodeError, TypeError):
            return

        if not isinstance(data, dict):
            return

        if not self.user.is_authenticated:
            return

        # Relay WebRTC signaling and whiteboard events.
        data["username"] = self.user.username

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "meeting_message",
                "data": data,
                "sender_channel": self.channel_name,
            }
        )

    def user_joined(self, event):
        if event.get("sender_channel") == self.channel_name:
            return

        self.send(text_data=json.dumps({
            "type": "join",
            "username": event.get("username", "Guest"),
        }))

    def meeting_message(self, event):
        if event.get("sender_channel") == self.channel_name:
            return

        self.send(text_data=json.dumps(event["data"]))

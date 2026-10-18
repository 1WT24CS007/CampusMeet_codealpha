import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.user = self.scope["user"]

        self.other_user_id = self.scope["url_route"]["kwargs"]["user_id"]

        user_ids = sorted([
            self.user.id,
            int(self.other_user_id)
        ])

        self.room_group_name = f"chat_{user_ids[0]}_{user_ids[1]}"
        print("USER:", self.user.username)
        print("ROOM:", self.room_group_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        print("MESSAGE RECEIVED:", text_data)
        data = json.loads(text_data)
        message = data["message"]

        Message.objects.create(
            sender=self.user,
            receiver_id=int(self.other_user_id),
            message=message
        )

        print("SENDING TO ROOM:", self.room_group_name)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": self.user.username,
            }
        )

    def chat_message(self, event):
        print("MESSAGE SENT TO BROWSER:", event)
        self.send(text_data=json.dumps({
            "message": event["message"],
            "username": event["username"],
        }))
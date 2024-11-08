import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
from .models import Conversacion, Mensaje

User = get_user_model()


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = str(self.scope["url_route"]["kwargs"]["room_name"])
        self.room_group_name = f"chat_{self.room_name}"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

        self.send(
            text_data=json.dumps(
                {"type": "connection_established", "message": "you are now connected!"}
            )
        )

    """ def disconnect(self, close_code):
        # Salir del grupo de la conversación en Redis
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        ) """

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json["message"]
        sender = self.scope["user"]
        conversation = Conversacion.objects.get(id=self.room_name)
        message = Mensaje.objects.create(
            conversation=conversation,
            message=message_content,
            sender=sender,
        )

        self.send(
            text_data=json.dumps(
                {
                    "type": "chat",
                    "message": message_content,
                    "sender": sender.username,
                    "timestamp": str(message.created),
                }
            )
        )

    def chat_message(self, event):
        self.send(
            text_data=json.dumps(
                {
                    "type": "chat",
                    "message": event["message"],
                    "sender": event["sender"],
                    "timestamp": event["timestamp"],
                }
            )
        )

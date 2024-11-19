import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
from .models import Conversacion, Mensaje
from django.utils import timezone


User = get_user_model()


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = str(self.scope["url_route"]["kwargs"]["room_name"])
        self.room_group_name = f"chat_{self.room_name}"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        print("WebSocket connected")

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
        print("WebSocket disconnected")

    def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get("action")
        print(f"Received action: {action}")

        if action == "send_message":
            message_content = data["message"]
            sender = self.scope["user"]
            conversation = Conversacion.objects.get(id=self.room_name)
            message = Mensaje.objects.create(
                conversation=conversation,
                message=message_content,
                sender=sender,
            )
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message_content,
                    "sender": sender.username,
                    "id": sender.id,
                    "timestamp": str(message.created),
                    "message_id": message.id,
                },
            )
            print(f"Message sent: {message_content}")

        elif action == "delete_message":
            message_id = data.get("message_id")
            print(f"Attempting to delete message with ID: {message_id}")
            try:
                message = Mensaje.objects.get(id=message_id)
                print(f"Mensaje encontrado: {message}")
                print(f"Mensaje encontrado: {message.message}")
                message.delete = timezone.now()
                message.save()

                if message.sender == self.scope["user"]:
                    message.delete = timezone
                    async_to_sync(self.channel_layer.group_send)(
                        self.room_group_name,
                        {
                            "type": "delete_message",
                            "message_id": message_id,
                            "deleted_at": str(message.delete),
                        },
                    )
                    print(f"Message deleted: {message_id}")
            except Mensaje.DoesNotExist:
                print("Message does not exist")

    def chat_message(self, event):
        self.send(
            text_data=json.dumps(
                {
                    "type": "chat",
                    "message": event["message"],
                    "sender": event["sender"],
                    "sender_id": event["id"],
                    "timestamp": event["timestamp"],
                    "message_id": event["message_id"],
                }
            )
        )

    def delete_message(self, event):
        self.send(
            text_data=json.dumps(
                {
                    "type": "delete_message",
                    "message_id": event["message_id"],
                }
            )
        )

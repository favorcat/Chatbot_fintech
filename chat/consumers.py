from channels.generic.websocket import WebsocketConsumer
import json
from . import sender

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        answer = sender.ChatbotMessageSender().req_message_send(message).json()['bubbles'][0]['data']['description']

        self.send(text_data=json.dumps({
            'message': answer
        }))
import json
import asyncio
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import numpy as np
from PIL import Image
import base64
from io import BytesIO
import chat.backend.ui_api
#import img_generator

from PIL import Image
import base64
from io import BytesIO



class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.Backend=chat.backend.ui_api.UiInterface()
        self.accept()
        
    def receive(self, text_data):
        
        text_data_json = json.loads(text_data)
        if(text_data_json['function']!=''):
            Boundfunc=getattr(self.Backend,text_data_json['function'])
            Boundfunc()
        message = text_data_json['message']
        print(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )
    def sendData(self, event):
        message = event['message']
        data= json.loads(message)
        self.send(text_data=json.dumps({
            'type':data['type'],
            'message':data['message']
        }))
    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'chat_message',
            'message':message
        }))
    def send_image(self):
        img = Image.new('RGB', (200, 200), color=tuple(np.random.choice(range(256),size=3)))
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
        # image_data =generate_image()
        self.send(text_data=json.dumps({
            'type':'image',
            'messages': img_str
        }))


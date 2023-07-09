from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import time
import threading

import numpy as np
from PIL import Image
import base64
from io import BytesIO
import chat.backend.ui_api
#import img_generator

from PIL import Image
import base64
from io import BytesIO
import json


def send_all(type,message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer. group_send)("test", {
    "type": "sendData",
    "message": json.dumps({'type':type,'message':message})
    })


def send_image():
    img = Image.new('RGB', (200, 200), color=tuple(np.random.choice(range(256),size=3)))
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    send_all('image',img_str)

run=False


def uistream():
    x=0

class UiInterface:
    counter=0
    
    def __init__(self):
        runloop=threading.Thread(target=self.run,args=[1])
        print("started")
        runloop.start()
        print("startedf")
        self.counter=0

    def getCounter(self):
        print(self.counter)
    
    def switchRun(self):
        global run 
        run= not run
        print(run)

    def run(self,input):
        while(True):
            self.counter+=1
            #print(self.counter)
            send_all("runvar",str(run))
            #send_all("chat_message","lala")
            #send_image()
            time.sleep(2)      

if __name__ == '__main__':
    Interface=UiInterface()

            

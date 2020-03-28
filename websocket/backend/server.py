import asyncio
import websockets
import io
import sys
import cv2
import json
import numpy as np
import imutils
from PIL import Image, ImageMode

sys.path.append('opencv')
sys.path.append('opencv/evertonsavio')
from face import executeOpenCV

async def QSocket(websocket, path):
    flag=0
    while True:
        message = await websocket.recv()
        frame = imutils.resize(np.array(Image.open(io.BytesIO(message))), width=450) #resizing image to maximum of 450 pixels. cv2.resize() can also do the same but in order to
        #maintain aspect ratio imutils.resize() is used.
        try:
            frame, flag = executeOpenCV(frame, flag)
        except: print('Aproxime-se da camera')
        #cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            #to cleanup the camera and close any open windows
            cv2.destroyAllWindows()
            break
        greeting = {"Hello": flag}
        await websocket.send(json.dumps(greeting))

        cv2.imshow("Frame", frame)
        
start_server = websockets.serve(QSocket, "127.0.0.1", 3333)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

        #pil_image = Image.open(io.BytesIO(message)) #.convert('RGB')
        #image.show()
        #open_cv_image = np.array(pil_image) 
        #print(open_cv_image)
        #open_cv_image = open_cv_image[:, :, ::-1].copy() 
        # now do with your images whatever you want. I used image.show to check it, it was spamming my monitor
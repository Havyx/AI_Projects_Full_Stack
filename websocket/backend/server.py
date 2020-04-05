import base64
import asyncio
import websockets
import json, codecs
from packages.face import reconhecimentoFacial

async def QSocket(websocket, path):
    flag=0
    while True:
        message = await websocket.recv()
        try:
            frame = reconhecimentoFacial(message, flag) #Linha5
        except: 
            print('Aproxime-se da camera')
        try:
            btframe = base64.b64encode(frame) #new_img = Image.fromarray(frame)
            await websocket.send(btframe) #await websocket.send(json.dumps(frame))
        except:
            print('Erro ao enviar bytes') 
        
start_server = websockets.serve(QSocket, "127.0.0.1", 3333)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

    #pil_image = Image.open(io.BytesIO(message)) #.convert('RGB')
    #image.show()
    #open_cv_image = np.array(pil_image) 
    #print(open_cv_image)
    #open_cv_image = open_cv_image[:, :, ::-1].copy() 
    # now do with your images whatever you want. I used image.show to check it, it was spamming my monitor
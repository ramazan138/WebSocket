import asyncio
import websockets
import time
""" Asenkron web socet"""
async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        
        name = "What's your name? "
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))
_counter=1
start=time.time()


asyncio.get_event_loop().run_until_complete(hello())

""" Hız Denemesi Yapmak için bunu Aktiv edin"""
# while True:

#     asyncio.get_event_loop().run_until_complete(hello())
#     _counter+=1
#     if(_counter%1000==0):
#         print(time.time()-start)    
#         start=time.time()

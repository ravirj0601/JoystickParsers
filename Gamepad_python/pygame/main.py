# -*- Conifidential Planys Technologies-*-

# Author :  Ravi Ranjan Rajak 
# Department:   Software Engineering
# Created on:   11-Apr-2023
# Created for:  Aarunya Project

## TODO
## 1. Replace the exit() implementation with something more reliable & elegant
## 2. Do we really need to have classes in here? Think & let's discuss
## 3. Read necessary configuration from a config file   



# import joystickMap
from threading import Thread
import time
from multiprocessing import process
import subprocess
import socketio
from aiohttp import web
import json


# with open("config.json") as f:
#     config = json.load(f)

# ipAdd = config['ipAdd']
# port = config['port']

readXbox = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sio = socketio.AsyncServer(async_mode='aiohttp')

app = web.Application()
sio.attach(app)


@sio.event
async def connect(sid, environ):
    print(sid, 'connected')


@sio.event
async def disconnect(sid):
    print(sid, 'disconnected')


@sio.event
async def command_listen(sid, data):
    global readXbox
    readXbox=data
   # print(readXbox)


def exit():
    file = "ps -aux | grep -i main.py | head -n 1 | awk '{print $2}'"
    pid = subprocess.check_output(file, shell=True).decode().strip()
    subprocess.run(['kill', '-9', pid])
    

class mainThread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        remoteControlerThread = RemoteControl()
        remoteControlerThread.start()


class RemoteControl(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while(True):   
            for i,element in enumerate(readXbox):
                if element != 0 :
                    match i:
                        case 0:
                            if float(readXbox[i]) > 0.03 or float(readXbox[i]) < -0.03: 
                                print('lx pressed: ', readXbox[i])
                                # print(readXbox[18])
                        case 1:
                            if float(readXbox[i]) > 0.03 or float(readXbox[i]) < -0.03:
                                print('ly pressed: ', readXbox[i])
                                # print(readXbox[18])
                        case 2:
                            if float(readXbox[i]) > 0.03 or float(readXbox[i]) < -0.03:
                                print('rx pressed: ', readXbox[i])

                            # print('A Button pressed: ', readXbox[i])
                            # print(readXbox[18])
                        case 3:
                            if float(readXbox[i]) > 0.03 or float(readXbox[i]) < -0.03:
                                print('ry pressed: ', readXbox[i])
                            # print('Y Button pressed: ', readXbox[i])
                            # print(readXbox[18])
                        case 4:
                            if float(readXbox[i]) > 0.03 or float(readXbox[i]) < -0.03:
                                print('lt pressed: ', readXbox[i])
                            # print('rb Button pressed: ', readXbox[i])
                            # print(readXbox[18])
                        case 5:
                            if float(readXbox[i]) > 0.03 or float(readXbox[i]) < -0.03:
                                print('rt pressed: ', readXbox[i])
                            # print('lb Button pressed: ', readXbox[i])
                            # print(readXbox[18])
                        case 6:
                            print('A Button pressed: ', readXbox[i])
                                # print(readXbox[18])
                        case 7:
                            print('Y Button pressed: ', readXbox[i])
                                # print(readXbox[18])
                        case 8:
                            print('x button pressed: ', readXbox[i])
                            # print(readXbox[18])
                        case 9:
                            print('b button pressed: ', readXbox[i])
                            # print(readXbox[18])
                        case 10:
                            print('Right Bumper button pressed: ', readXbox[i])
                        case 11:
                            print('Left Bumper button pressed: ', readXbox[i])
                            # print(readXbox[18])
                        case 12:
                            print('Stop Button pressed: ', readXbox[i])
                            # print(readXbox[18])
                            try:
                                exit()
                            except KeyboardInterrupt:
                                exit()
                            print('up or down Dpad button pressed: ', readXbox[i])
                        case 13:
                            print('Start button pressed: ', readXbox[i])
                            # print(readXbox[18])
                        case 14:
                            print('XboxButton pressed: ', readXbox[i])
                            
                        case 15:    
                            print('Record Button pressed: ', readXbox[i])
                            # print(readXbox[18])
                        # case 16:
                        #     print('Xbox button pressed: ', readXbox[i])
                        #     # print(readXbox[18])
                        # case 17:
                        #     print('lt button pressed: ', readXbox[i])
                        #     # print(readXbox[18])
                        # case 18:
                        #     print('rt button pressed: ', readXbox[i])
                        # case 19:
                        #     print('Record button pressed: ', readXbox[i])
                        #     # print(readXbox[18])
            time.sleep(0.02)


if __name__ == "__main__":
    mainThreadObj = mainThread()
    mainThreadObj.start()
    web.run_app(app, host="10.0.1.18", port=8989)
    

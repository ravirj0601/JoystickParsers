'''
The application uses components that are open source. You can find the source code of 
their open source projects along with license information below. We would like to 
acknowledge and thank these developers for their contributions to open source.

# Author : Kevin Hughes
# Copyright (c) 2017 Kevin Hughes
# Original Code: https://github.com/kevinhughes27/TensorKart/blob/master/utils.py
# LICENSE: (MIT) https://github.com/kevinhughes27/TensorKart/blob/master/LICENSE.txt
'''

##
## TODO 1. Use the latest SupportLib Logger from SSS
##      2. Reorganize the code to read from config.json through import based utility


from inputs import get_gamepad
import math
import sys
import socketio
import logging
import config
from datetime import datetime

cfg = config.Config('main.cfg')
# with open("config.json") as f:
#     config = json.load(f)

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('Xbox.log')
sh = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s",
                              datefmt='%a, %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(sh)


MAX_TRIG_VAL = math.pow(2, 8)
MAX_JOY_VAL = math.pow(2, 15)


server_IP = cfg['server_IP']
LeftJoystickY = cfg['LeftJoystickY']
LeftJoystickX = cfg['LeftJoystickX']
RightJoystickY = cfg['RightJoystickY']
RightJoystickX = cfg['RightJoystickX']
LeftTrigger = cfg['LeftTrigger']
RightTrigger = cfg['RightTrigger']
LeftBumper = cfg['LeftBumper']
RightBumper = cfg['RightBumper']
A = cfg['A']
X = cfg['X']
Y = cfg['Y']
B = cfg['B']
Back = cfg['Back']
Start = cfg['Start']
LeftDPad = cfg['LeftDPad']
RightDPad = cfg['RightDPad']
UpDPad = cfg['UpDPad']
DownDPad = cfg['DownDPad']
Kuchb = cfg['Kuchb']
Xbox = cfg['Xbox']

def read():
    lx = LeftJoystickX 
    ly = LeftJoystickY 
    rx = RightJoystickX 
    ry = RightJoystickY 
    a = A 
    y = Y 
    rb = RightBumper 
    lb = LeftBumper 
    x = X 
    b = B 
    rd = LeftDPad 
    ud = UpDPad 
    lt = LeftTrigger 
    rt = RightTrigger 
    stop = Back 
    start = Start 
    menu = Kuchb 
    xbox = Xbox  
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S:%f")
    data_sent = current_time
    
    print([round(lx,3), round(ly,2), a, y, rb,lb,round(rx,3), round(ry,3),x,b,rd,ud,stop,start,menu,xbox,lt,rt,data_sent])
    return [round(lx,3), round(ly,2), a, y, rb,lb,round(rx,3), round(ry,3),x,b,rd,ud,stop,start,menu,xbox,lt,rt,data_sent]


sio2 = socketio.Client()
    
@sio2.event
def connect():
    print('connected')

@sio2.event
def connect_error(data):
    print("The connection failed!. Connecting again...")
    logger.info(data)

@sio2.event
def disconnect():
    print('disconnected')



def main():
    global LeftJoystickX
    global LeftJoystickY
    global RightJoystickX
    global RightJoystickY
    global LeftTrigger
    global RightTrigger
    global LeftBumper
    global RightBumper
    global A
    global B
    global X
    global Y
    global LeftThumb,RightThumb,Back,Start, LeftDPad, RightDPad, UpDPad,DownDPad
    global server_IP
    global Xbox
    global Kuchb
    sio2.connect(server_IP)
    
    while True:
        events = get_gamepad() 
        for event in events:
            if event.code == 'ABS_Y':
                LeftJoystickY = event.state / MAX_JOY_VAL # normalize between -1 and 1
            elif event.code == 'ABS_X':
                LeftJoystickX = event.state / MAX_JOY_VAL # normalize between -1 and 1
            elif event.code == 'ABS_RY':
                RightJoystickY = event.state / MAX_JOY_VAL # normalize between -1 and 1
            elif event.code == 'ABS_RX':
                RightJoystickX = event.state / MAX_JOY_VAL # normalize between -1 and 1
            elif event.code == 'ABS_Z':
                LeftTrigger = event.state / MAX_TRIG_VAL # normalize between 0 and 1
            elif event.code == 'ABS_RZ':
                RightTrigger = event.state / MAX_TRIG_VAL # normalize between 0 and 1
            elif event.code == 'BTN_TL':
                LeftBumper = event.state
            elif event.code == 'BTN_TR':
                RightBumper = event.state
            elif event.code == 'BTN_SOUTH':
                A = event.state
            elif event.code == 'BTN_NORTH':
                X = event.state
            elif event.code == 'BTN_WEST':
                Y = event.state
            elif event.code == 'BTN_EAST':
                B = event.state
            elif event.code == 'BTN_THUMBL':
                LeftThumb = event.state
            elif event.code == 'BTN_THUMBR':
                RightThumb = event.state
            elif event.code == 'BTN_SELECT':
                Back = event.state
            elif event.code == 'BTN_START':
                Start = event.state
            elif event.code == 'KEY_RECORD':
                Kuchb = event.state
            elif event.code == 'BTN_MODE':
                Xbox = event.state
            elif event.code == 'ABS_HAT0X':
                LeftDPad = event.state
            # python-socketio
            elif event.code == 'ABS_HAT0X':
                RightDPad = event.state
            elif event.code == 'ABS_HAT0Y':
                UpDPad = event.state
            elif event.code == 'ABS_HAT0Y':
                DownDPad = event.state
            if (sio2.connected):
                sio2.emit('command_listen',read())
                # print(msg)
            else:
                print('Server is disconnected, Waiting for Server')

main()



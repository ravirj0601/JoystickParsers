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
from inputs import get_key
import math
import sys
import socketio
import logging
import json

with open("config.json") as f:
    config = json.load(f)

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


server_IP = config['server_IP']
LeftJoystickY = config['LeftJoystickY']
LeftJoystickX = config['LeftJoystickX']
RightJoystickY = config['RightJoystickY']
RightJoystickX = config['RightJoystickX']
LeftTrigger = config['LeftTrigger']
RightTrigger = config['RightTrigger']
LeftBumper = config['LeftBumper']
RightBumper = config['RightBumper']
A = config['A']
X = config['X']
Y = config['Y']
B = config['B']
Back = config['Back']
Start = config['Start']
LeftDPad = config['LeftDPad']
RightDPad = config['RightDPad']
UpDPad = config['UpDPad']
DownDPad = config['DownDPad']
Kuchb = config['Kuchb']
Xbox = config['Xbox']

w = config['w']
a = config['a']
d = config['d']
s = config['s']
up = config['up']
down = config['down']
left = config['left']
right = config['right']
e = config['e']
r = config['r']
z = config['z']
x = config['x']
k = config['k']
j = config['j']
i = config['i'] 
l = config['l']
space = config['space']
f = config['f']
t = config['t']
y = config['y']
v = config['v']
b = config['b']
n = config['n']
c = config['c']

def readk():
    print([w,a,d,s,up,down,left,right,e,r,z,x,k,j,i,l,space,f,t,y,v,b,n,c])    
    return [w,a,d,s,up,down,left,right,e,r,z,x,k,j,i,l,space,f,t,y,v,b,n,c]    


def read(): # return the buttons/triggers that you care about in this methode
    lx = LeftJoystickX
    ly = LeftJoystickY
    rx = RightJoystickX
    ry = RightJoystickY
    a = A # A button
    y = X # Y button
    rb = RightBumper
    lb = LeftBumper
    x  = Y #X
    b =  B #B
    rd = RightDPad  #Dpad Buttons 
    ld = LeftDPad   #Dpad Buttons
    ud = UpDPad     #Dpad Buttons
    dd = DownDPad   #Dpad Buttons
    
    lt = LeftTrigger
    rt  = RightTrigger
    stop = Back
    start = Start
    menu = Kuchb
    xbox = Xbox
    
    print([round(lx,3), round(ly,2), a, y, rb,lb,round(rx,3), round(ry,3),x,b,rd,ld,ud,dd,stop,start,menu,xbox,lt,rt])
    return [round(lx,3), round(ly,2), a, y, rb,lb,round(rx,3), round(ry,3),x,b,rd,ld,ud,dd,stop,start,menu,xbox,lt,rt]


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
    global LeftJoystickXL
    global LeftJoystickXR
    global LeftJoystickY
    global LeftJoystickYU
    global LeftJoystickYD
    global RightJoystickX
    global RightJoystickXL
    global RightJoystickXR
    global RightJoystickY
    global RightJoystickYU
    global RightJoystickYD
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
        events = get_gamepad() #+ get_key()
        for event in events:
            # print(event.code)
            if event.ev_type == 'Key':
                if event.code == 'KEY_A':
                    LeftJoystickXL = event.state
                elif event.code == 'KEY_D':
                    LeftJoystickXR = event.state
                elif event.code == 'KEY_W':
                    LeftJoystickYU = event.state
                elif event.code == 'KEY_S':
                    LeftJoystickYD = event.state
                elif event.code == 'KEY_UP':
                    RightJoystickYU = event.state
                elif event.code == 'KEY_DOWN':
                    RightJoystickY = event.state
                elif event.code == 'KEY_LEFT':
                    RightJoystickXL = event.state
                elif event.code == 'KEY_RIGHT':
                    RightJoystickXR = event.state
                elif event.code == 'KEY_E':
                    RightJoystickX = event.state
                elif event.code == 'KEY_R':
                    RightTrigger = event.state
                elif event.code == 'KEY_Z':
                    LeftBumper = event.state
                elif event.code == 'KEY_X':
                    RightBumper = event.state
                elif event.code == 'KEY_K':
                    A = event.state
                elif event.code == 'KEY_J':
                    X = event.state
                elif event.code == 'KEY_I':
                    Y = event.state
                elif event.code == 'KEY_L':
                    B = event.state
                elif event.code == 'KEY_SPACE':
                    Back = event.state
                elif event.code == 'KEY_F':
                    Start = event.state
                elif event.code == 'KEY_T':
                    LeftDPad = event.state
                elif event.code == 'KEY_Y':
                    RightDPad = event.state
                elif event.code == 'KEY_V':
                    UpDPad = event.state
                elif event.code == 'KEY_B':
                    DownDPad = event.state
                elif event.code == 'KEY_N':
                    Kuchb = event.state
                elif event.code == 'KEY_C':
                    Xbox = event.state
                if (sio2.connected):
                    sio2.emit('command_listen',readk())
                    # print(msg)
                else:
                    print('Server is disconnected, Waiting for Server')
                
            elif event.ev_type == 'Absolute':
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
                elif event.code == 'BTN_RECORD':
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



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
# TODO 1. Use the latest SupportLib Logger from SSS
# 2. Reorganize the code to read from config.json through import based utility


from inputs import get_gamepad
from inputs import get_key
import math
import sys
import logging
import socketio
import configparser

dynamic_cfg = configparser.ConfigParser()
dynamic_cfg.read('dynamic.ini')

# logger = logging.getLogger('')
# logger.setLevel(logging.DEBUG)
# fh = logging.FileHandler('Xbox.log')
# sh = logging.StreamHandler(sys.stdout)
# formatter = logging.Formatter("[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s",
#                               datefmt='%a, %d %b %Y %H:%M:%S')
# fh.setFormatter(formatter)
# sh.setFormatter(formatter)
# logger.addHandler(fh)
# logger.addHandler(sh)

MAX_TRIG_VAL = math.pow(2, 8)
MAX_JOY_VAL = math.pow(2, 15)

Slx = 0
Slxm = 0
Sly = 0
Slym = 0
Srx = 0
Srxm = 0
Sry = 0
Srym = 0
SA = 0
SY = 0
Srb = 0
Slb = 0
SX = 0
SB = 0
Srd = 0
Sld = 0
Sud = 0
Sdd = 0
Slt = 0
Srt = 0
Sstop = 0
Sstart = 0
Srecord = 0
Smenu = 0
Sxbox = 0
code = ''

device = dynamic_cfg.get('system', 'device')
server_IP = dynamic_cfg.get('system', 'serverip')
lx = dynamic_cfg.get(device, 'lx')
lxm = dynamic_cfg.get(device, 'lxm')
ly = dynamic_cfg.get(device, 'ly')
lym = dynamic_cfg.get(device, 'lym')
rx = dynamic_cfg.get(device, 'rx')
rxm = dynamic_cfg.get(device, 'rxm')
ry = dynamic_cfg.get(device, 'ry')
rym = dynamic_cfg.get(device, 'rym')
a = dynamic_cfg.get(device, 'a')
y = dynamic_cfg.get(device, 'y')
rb = dynamic_cfg.get(device, 'rb')
lb = dynamic_cfg.get(device, 'lb')
x = dynamic_cfg.get(device, 'x')
b = dynamic_cfg.get(device, 'b')
rd = dynamic_cfg.get(device, 'rd')
ld = dynamic_cfg.get(device, 'ld')
ud = dynamic_cfg.get(device, 'ud')
dd = dynamic_cfg.get(device, 'dd')
lt = dynamic_cfg.get(device, 'lt')
rt = dynamic_cfg.get(device, 'rt')
stop = dynamic_cfg.get(device, 'back')
start = dynamic_cfg.get(device, 'start')
Record = dynamic_cfg.get(device, 'record')
xbox = dynamic_cfg.get(device, 'xbox')

def read():  # return the buttons/triggers that you care about in this methode
    Xlx = Slx
    Xlxm = Slxm
    Xly = Sly
    Xlym = Slym
    Xrx = Srx
    Xrxm = Srxm
    Xry = Sry
    Xrym = Srym
    Xa = SA  # A button
    Xy = SX  # Y button
    Xrb = Srb
    Xlb = Slb
    Xx = SY  # X
    Xb = SB  # B
    Xrd = Srd  # Dpad Buttons
    Xld = Sld  # Dpad Buttons
    Xud = Sud  # Dpad Buttons
    Xdd = Sdd  # Dpad Buttons
    Xlt = Slt
    Xrt = Srt
    Xstop = Sstop
    Xstart = Sstart
    Xrecord = Srecord
    Xxbox = Sxbox
    Xcode = code
    # print([round(Xlx, 3), round(Xly, 2), Xa, Xy, Xrb, Xlb, round(Xrx, 3), round(Xry, 3), Xx,
        #   Xb, Xrd, Xld, Xud, Xdd, Xstop, Xstart, Xxbox, Xlt, Xrt, Xrecord, Xlxm, Xlym, Xrxm, Xrym, Xcode])
    return [round(Xlx, 3), round(Xly, 2), Xa, Xy, Xrb, Xlb, round(Xrx, 3), round(Xry, 3), Xx, Xb, Xrd, Xld, Xud, Xdd, Xstop, Xstart, Xxbox, Xlt, Xrt, Xrecord, Xlxm, Xlym, Xrxm, Xrym, Xcode]

sio2 = socketio.Client()

@sio2.event
def connect():
    print('connected')


@sio2.event
def connect_error(data):
    print("The connection failed!. Connecting again...")


@sio2.event
def disconnect():
    print('disconnected')


def main():
    global Slx
    global Slxm
    global Sly
    global Slym
    global Srx
    global Srxm
    global Sry
    global Srym
    global SA   # A button
    global SX   # Y button
    global Srb
    global Slb
    global SY  # X
    global SB  # B
    global Srd  # Dpad Buttons
    global Sld  # Dpad Buttons
    global Sud  # Dpad Buttons
    global Sdd  # Dpad Buttons
    global Slt
    global Srt
    global Sstop
    global Sstart
    global Srecord
    global Sxbox
    global code

    sio2.connect(server_IP)
    while True:
        if device == 'Keyboard':
            events = get_key()
            for event in events:
                if event.code == ly:
                    Sly = event.state
                    code = ly
                elif event.code == lym:
                    Slym = event.state
                    code = lym
                elif event.code == lx:
                    Slx = event.state
                    code = lx
                elif event.code == lxm:
                    Slxm = event.state
                    code = lxm
                elif event.code == ry:
                    Sry = event.state
                    code = ry
                elif event.code == rym:
                    Srym = event.state
                    code = rym
                elif event.code == rx:
                    Srx = event.state
                    code = rx
                elif event.code == rxm:
                    Srxm = event.state
                    code = rxm
                elif event.code == lt:
                    Slt = event.state
                    code = lt
                elif event.code == rt:
                    Srt = event.state
                    code = rt
        elif device == 'Xbox':
            events = get_gamepad()
            for event in events:
                if event.code == ly:
                    Sly = event.state / MAX_JOY_VAL  # normalize between -1 and 1
                    code = ly
                elif event.code == lx:
                    Slx = event.state / MAX_JOY_VAL  # normalize between -1 and 1
                    code = lx
                elif event.code == ry:
                    Sry = event.state / MAX_JOY_VAL  # normalize between -1 and 1
                    code = ry
                elif event.code == rx:
                    Srx = event.state / MAX_JOY_VAL  # normalize between -1 and 1
                    code = rx
                elif event.code == lt:
                    Slt = event.state / MAX_TRIG_VAL  # normalize between 0 and 1
                    code = lt
                elif event.code == rt:
                    Srt = event.state / MAX_TRIG_VAL  # normalize between 0 and 1
                    code = rt
        for event in events:
            if event.code == lb:
                Slb = event.state
                code = lb
            elif event.code == rb:
                Srb = event.state
                code = rb
            elif event.code == a:
                SA = event.state
                code = a
            elif event.code == x:
                SX = event.state
                code = x
            elif event.code == y:
                SY = event.state
                code = y
            elif event.code == b:
                SB = event.state
                code = b
            elif event.code == stop:
                Sstop = event.state
                code = stop
            elif event.code == start:
                Sstart = event.state
                code = start
            elif event.code == Record:
                Srecord = event.state
                code = Record
            elif event.code == xbox:
                Sxbox = event.state
                code = xbox
            elif event.code == ld:
                Sld = event.state
                code = ld
            elif event.code == rd:
                Srd = event.state
                code = rd
            elif event.code == ud:
                Sud = event.state
                code = ud
            elif event.code == dd:
                Sdd = event.state
                code = dd
            if (sio2.connected):
                sio2.emit('command_listen', read())
            else:
                print('Server is disconnected, Waiting for Server')

main()
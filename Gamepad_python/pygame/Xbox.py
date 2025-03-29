from inputs import get_gamepad
from inputs import get_key
import math
import sys
import logging
import socketio
import configparser
import pygame

pygame.init()
pygame.joystick.init()

num_joysticks = pygame.joystick.get_count()

if num_joysticks > 0:
    controller = pygame.joystick.Joystick(0)
    controller.init()
    device = controller.get_name()
    print("Controller connected:", device)
else:
    print("No controller detected.")


dynamic_cfg = configparser.ConfigParser()
dynamic_cfg.read('dynamic.ini')


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

server_IP = "http://10.0.1.18:8000"
# dynamic_cfg.get('system', 'serverip')



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
    Xrecord = Sshare
    Xxbox = Sxbox
    # Xcode = code
    print([round(Xlx, 3), round(Xly, 2),round(Xrx, 3), round(Xry, 3),  round(Xlt, 3), round(Xrt, 3), Xa, Xy, Xx, Xb, Xrb, Xlb, 
             Xstop, Xstart, Xxbox, Xrecord, Xrd, Xld, Xud, Xdd, Xlxm, Xlym, Xrxm, Xrym])
    return [round(Xlx, 3), round(Xly, 2),round(Xrx, 3), round(Xry, 3),  round(Xlt, 3), round(Xrt, 3), Xa, Xy, Xx, Xb, Xrb, Xlb, 
             Xstop, Xstart, Xxbox, Xrecord, Xrd, Xld, Xud, Xdd, Xlxm, Xlym, Xrxm, Xrym]


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
    global Slstick
    global Srstick
    global Sshare

    sio2.connect(server_IP)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  

            if event.type == pygame.JOYBUTTONDOWN:
                # print("Joystick button pressed.")
                if event.button == 0:
                    controller.rumble(0, 0.7, 500) 
        
            axes = controller.get_numaxes()
            # print("No of Axes : " , axes)
            buttons = controller.get_numbuttons()
            # print("No of buttons : ", buttons)
            hats = controller.get_numhats()
            
            for i in range(axes):
                axis = controller.get_axis(i)
                if i == 0:
                    Sly = axis #/ MAX_JOY_VAL
                elif i == 1:
                    Slx = axis #/ MAX_JOY_VAL
                elif i == 2:
                    Sry = axis #/ MAX_JOY_VAL
                elif i == 3:
                    Srx = axis #/ MAX_JOY_VAL
                elif i == 4:
                    Slt = axis #/ MAX_TRIG_VAL
                elif i == 5:
                    Srt = axis #/ MAX_TRIG_VAL
            
            for i in range(buttons):
                button = controller.get_button(i)
                if i == 0:
                    SA = button
                elif i == 1:
                    SB = button
                elif i == 2:
                    SX = button
                elif i == 3:
                    SY  = button
                elif i == 4:
                    Slb = button
                elif i == 5:
                    Srb = button
                elif i == 6:
                    Sstop = button
                elif i == 7:
                    Sstart = button
                elif i == 8:
                    Sxbox = button
                elif i == 9:
                    Slstick = button
                elif i == 10:
                    Srstick = button
                elif i == 11:
                    Sshare = button   
            for i in range(hats):
                hat = controller.get_hat(i)
        
            if (sio2.connected):
                sio2.emit('command_listen', read())
            else:
                print('Server is disconnected, Waiting for Server')
            read()

main()

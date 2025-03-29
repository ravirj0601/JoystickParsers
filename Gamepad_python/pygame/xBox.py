import pygame
import sys
import time
import math
pygame.init()
pygame.joystick.init()
num_joysticks = pygame.joystick.get_count()

MAX_TRIG_VAL = math.pow(2, 8)
MAX_JOY_VAL = math.pow(2, 15)


if num_joysticks > 0:
    controller = pygame.joystick.Joystick(0)
    controller.init()
    print("Controller connected:", controller.get_name())
    
    while True:
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  

            if event.type == pygame.JOYBUTTONDOWN:
                # print("Joystick button pressed.")
                if event.button == 0:
                    controller.rumble(0, 0.7, 500)

            name = controller.get_name()
            # print(name)
            power_level = controller.get_power_level()
            # print(power_level)
            axes = controller.get_numaxes()
            # print("No of Axes : " , axes)
            buttons = controller.get_numbuttons()
            # print("No of buttons : ", buttons)
            hats = controller.get_numhats()
            
            for i in range(axes):
                axis = controller.get_axis(i)
                if i == 0:
                    ly = axis #/ MAX_JOY_VAL
                elif i == 1:
                    lx = axis #/ MAX_JOY_VAL
                elif i == 2:
                    ry = axis #/ MAX_JOY_VAL
                elif i == 3:
                    rx = axis #/ MAX_JOY_VAL
                elif i == 4:
                    lt = axis #/ MAX_TRIG_VAL
                elif i == 5:
                    rt = axis #/ MAX_TRIG_VAL
            
            for i in range(buttons):
                button = controller.get_button(i)
                if i == 0:
                    a = button
                elif i == 1:
                    b = button
                elif i == 2:
                    x = button
                elif i == 3:
                    y = button
                elif i == 4:
                    lb = button
                elif i == 5:
                    rb = button
                elif i == 6:
                    back = button
                elif i == 7:
                    start = button
                elif i == 8:
                    lstick = button
                elif i == 9:
                    rstick = button
                elif i == 10:
                    guide = button
                elif i == 11:
                    rt = button
                    
            for i in range(hats):
                hat = controller.get_hat(i)
                
        print(ly, lx, rx, ry, lt, rt, a, b, x, y, lb, rb, back, start, lstick, rstick, guide)
              
        # Limit to 30 frames per second.
        clock.tick(30)    

pygame.quit()  

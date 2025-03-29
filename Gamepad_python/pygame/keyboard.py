import pygame
import sys
pygame.init()
display = pygame.display.set_mode((1, 1))

# key_A = pygame.K_a


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
        if event.type == pygame.KEYDOWN:
            # print("Presesd this Key")
            if event.key == 97:
                print("Pressed A key")
                # print()
            if event.key == 98:
                print("Pressed B key")
                # print(event.key)
            if event.key == 120:
                print("Pressed X key")
                # print(event.key)
            if event.key == 121:
                print("Pressed Y key")
                # print(event.key)
    # pressed_keys = pygame.key.get_pressed()
    # if pressed_keys[K_a]:
    #     print("Key A has been pressed...")
        
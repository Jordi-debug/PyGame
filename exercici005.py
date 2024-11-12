#!/usr/bin/env python3

import math
import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils1

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    global list

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    utils1.draw_grid(pygame, screen, 50)
    
    # Centre de la finstra
    center_x, center_y = int(screen.get_width() / 2), int(screen.get_height() / 2)
    
    # Paràmetres de l'espiral rectangular
    x, y = center_x, center_y
    direction = 0  
    aumento = 15
    # Controla el nombre de voltes de l'espiral (25)
    #right, up, left, down
    for _ in range(25):
        if direction == 0:
            finX, finY = center_x + aumento, center_y
        elif direction == 1:
            finX, finY = center_x, center_y - aumento
        elif direction == 2:
            finX, finY = center_x - aumento, center_y
        elif direction == 3:
            finX, finY = center_x, center_y + aumento
        
        pygame.draw.line(screen, RED, (center_x, center_y), (finX, finY),5)
        center_x = finX
        center_y = finY
        direction = (direction + 1 ) % 4
        aumento += 15

    pygame.display.update()

if __name__ == "__main__":
    main()
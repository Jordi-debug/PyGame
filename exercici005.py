#!/usr/bin/env python3

import math
import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

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
    utils.draw_grid(pygame, screen, 50)
    
    # Centre de la finstra
    center_x, center_y = int(screen.get_width() / 2), int(screen.get_height() / 2)
    
    # Paràmetres de l'espiral rectangular
    x, y = center_x, center_y
    direction = 0  
    
    # Controla el nombre de voltes de l'espiral (25)
    aumento = 15
    for _ in range(25):  
        # Calcular el punt final de la línia
        #right, up, left, dwn
        if direction == 0:
            fin_x, fin_y = center_x + aumento, center_y
        elif direction == 1:
            fin_x, fin_y = center_x, center_y - aumento
        elif direction == 2:
            fin_x, fin_y = center_x - aumento, center_y
        elif direction == 3:
            fin_x, fin_y = center_x, center_y + aumento
        
        # Dibuixar la línia
        pygame.draw.line(screen, (234,134,34),(center_x, center_y),(fin_x, fin_y),4)
        # Actualitzar el punt inicial per a la següent línia
        center_x, center_y = fin_x, fin_y
        # Canviar la direcció i augmentar la longitud
        direction = (direction + 1) % 4
        aumento += 15
        # Augmentar la longitud per expandir l'espiral

    pygame.display.update()

if __name__ == "__main__":
    main()
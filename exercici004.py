#!/usr/bin/env python3

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

# Llista aleatòria
listCord = []

# Bucle de l'aplicació
def main():
    global listCord

    listCord = []

    is_looping = True

    window_width, window_height = screen.get_size()  # Obtenir els límits de la finestra

    for _ in range(0,11):
        listCord.append((random.randint(0, window_width), random.randint(0, window_height)))
        
    
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
    global listCord

# Dibuixar
def app_draw():
    global listCord
    window_width, window_height = screen.get_size()

    screen.fill(WHITE)
    utils1.draw_grid(pygame, screen, 50)

    pygame.draw.polygon(screen, (121,212,122), listCord, 5)

    

    pygame.display.update()

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils1

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (127, 184, 68)
YELLOW = (240, 187, 64)
ORANGE = (226, 137, 50)
RED = (202, 73, 65)
PURPLE = (135, 65, 152)
BLUE  = (75, 154, 217)
colors = [GREEN, YELLOW, ORANGE, RED, PURPLE, BLUE]
original_colors = colors.copy()
pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')
clicked = False
released = False
# Bucle de l'aplicació
def main():
    global clicked
    global released
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
    global colors
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            colors = [BLACK]*len(colors)
        if event.type == pygame.MOUSEBUTTONUP:
            colors = original_colors.copy()
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    global clicked
    global released
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils1.draw_grid(pygame, screen, 50)

    # Dibuixar quadres
    for q in range (0, len(colors)):
        x = 50 + q*100
        pygame.draw.rect(screen, colors[q],(x,50,50,50))

    for q in range (0, len(colors)):
        x = 75 + q*100
        pygame.draw.circle(screen, colors[q], (x,175),25,3)
    
    for q in range (0,len(colors)):
        r = 25*q
        g = 25*q
        b = 25*q
        x = 50 + q*100 + 25
        draw_polygon(screen,(r,g,b),(x,275),25,3,angle_offset=(math.pi / 3))
        draw_polygon(screen, (r,g,b),(x, 375),25,5,angle_offset=(math.pi / 3))

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

def draw_polygon(screen, color, center, radius, num_vertices, angle_offset=(math.pi / 3)):
    points = [
        (
            center[0] + radius * math.cos(angle_offset + i * 2 * math.pi / num_vertices),
            center[1] + radius * math.sin(angle_offset + i * 2 * math.pi / num_vertices)
        )
        for i in range(num_vertices)
    ]
    pygame.draw.polygon(screen, color, points)


if __name__ == "__main__":
    main()
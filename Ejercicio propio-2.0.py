import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
import random

# Definir colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

WIDTH = 50
HEIGHT = 50

pygame.init()
clock = pygame.time.Clock()
color = BLACK


# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Definir les dades // Vamos hacer que el cuadarado se mueva por la pantalla haciendo click o manteniendo pulsado
#La anchura y la altura las he definido como constantes
square_x = 50
square_y = 50
clicked = False
# Bucle de l'aplicació
def main():
    is_looping = True
    #global color
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
    global clicked
    #Para hacer que nos siga el ratón simplemente sin clickar quitamos los events de apretar
    for event in pygame.event.get():
        """if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False"""
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    global square_x, square_y, color
    mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
    r,g,b = random.randint(1,255), random.randint(1,255),random.randint(1,255)

    square_x = mouse_x
    square_y = mouse_y
    color = (r,g,b) #Para que sea un teclado de disco
    


# Dibuixar
def app_draw():
    global color
    # Pintar el fons de blanc
    screen.fill(WHITE)
    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)


    pygame.draw.rect(screen, color, (square_x, square_y, WIDTH, HEIGHT))




    
    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()
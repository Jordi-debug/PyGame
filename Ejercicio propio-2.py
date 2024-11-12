import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

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

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    global square_x, square_y, color
    mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

    if clicked:
        square_x = mouse_x
        square_y = mouse_y
        color = MAGENTA
    
    if not clicked: #Aquí no hace falta indicar la posición si desclickeamos porque se va a quedar en el sitio donde nosotros lo hayamos dejado
        color = CYAN

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
import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils1

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 200)
GREEN = (0,254,32)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Definir les dades
width = 200
height = 200
square_x = 100
square_y = 100
clicked = False
color = BLACK
get_big = True
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
    global clicked,get_mini, get_big,width,height
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True #Ponerlo en una variable asi nos srive para poder dejarlo pulsado
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    global square_y, square_x, color,width,height, get_big
    mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

    if  clicked and square_x <= mouse_x <= square_x + width and square_y <= mouse_y <= square_y + height:
        color = GREEN
    else:
        color = (0,50,50)
# Dibuixar
def app_draw():
    global color
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils1.draw_grid(pygame, screen, 50)

    pygame.draw.rect(screen, color, (square_x, square_y, width, height))

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()
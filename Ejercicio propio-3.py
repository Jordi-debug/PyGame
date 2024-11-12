import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 200)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
SOFT_RED = (244, 67, 54)
SOFT_GREEN = (76, 175, 80)
SOFT_BLUE = (33, 150, 243)
SOFT_YELLOW = (255, 235, 59)
SOFT_ORANGE = (255, 152, 0)
SOFT_PURPLE = (156, 39, 176)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')
color = SOFT_PURPLE
move_up = move_down = move_left = move_right = False
square_x = 50
square_y = 50
speed = 5

# Definir les dades

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
    global move_left , move_right , move_up , move_down

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
    
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    global color, move_down, move_left, move_right, move_up,square_y, square_x
    
    if move_up:
        square_y -= speed
        color = CYAN
    elif move_down:
        square_y += speed
        color = SOFT_BLUE
    elif move_right:
        square_x += speed
        color = SOFT_GREEN
    elif move_left:
        square_x -= speed
        color = SOFT_RED

# Dibuixar
def app_draw():
    global color
    # Pintar el fons de blanc
    screen.fill(WHITE)
    
    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    pygame.draw.rect(screen, color, (square_x, square_y,50,50))





    
    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()
import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils1
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 120, 200)
GREEN = (0,254,32)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
DARK_GRAY = (64, 64, 64)
GRAY = (128, 128, 128)
LIGHT_GRAY = (192, 192, 192)
SOFT_RED = (244, 67, 54)
SOFT_GREEN = (76, 175, 80)
SOFT_BLUE = (33, 150, 243)
SOFT_YELLOW = (255, 235, 59)
SOFT_ORANGE = (255, 152, 0)
SOFT_PURPLE = (156, 39, 176)
PASTEL_PINK = (255, 182, 193)
PASTEL_GREEN = (119, 221, 119)
PASTEL_BLUE = (173, 216, 230)
PASTEL_PURPLE = (216, 191, 216)
pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')
move_left = move_right = False
radius = 25
circle_x = 25
circle_y = 300
color = BLACK
width = 640
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
    
    global move_left, move_right

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    global move_left, move_right, circle_x, circle_y,width,radius

    delta_time = clock.get_time() / 1000.0
    size = 10 + (circle_x / 8)
    speed = 100*delta_time

    if move_right:
        circle_x += speed
        if circle_x + radius >= screen.get_width():
            move_right = False
    else:
        move_right = False
    
    if move_left:
        circle_x -= speed
        if circle_x - radius <= 0:
            move_left = False
    else:
        move_left = False
    
    radius = size

# Dibuixar
def app_draw():
    global color, radius, circle_y, circle_x
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils1.draw_grid(pygame, screen, 50)
    font_intro = pygame.font.SysFont("Arial",34)
    font_text = font_intro.render("Apreta les tecles (left/right)", True, BLACK)
    screen.blit(font_text,(50,50))

    pygame.draw.circle(screen, BLACK, (circle_x, circle_y),radius)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()
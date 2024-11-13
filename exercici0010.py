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
rectangles = [
    { "rect": { "x": 50, "y": 100, "width": 250, "height": 50 }, "color": RED },
    { "rect": { "x": 50, "y": 200, "width": 100, "height": 200 }, "color": DARK_GRAY },
    { "rect": { "x": 200, "y": 200, "width": 100, "height": 100 }, "color": BLUE },
    { "rect": { "x": 200, "y": 350, "width": 400, "height": 50 }, "color": MAGENTA },
    { "rect": { "x": 350, "y": 100, "width": 50, "height": 200 }, "color": PASTEL_BLUE },
    { "rect": { "x": 450, "y": 100, "width": 150, "height": 100 }, "color": GREEN },
    { "rect": { "x": 450, "y": 250, "width": 150, "height": 50 }, "color": PASTEL_PINK }
]
# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')
collide = -1


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
    global dragging, clicked

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    global collide

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for rect in rectangles:
        width = rect["rect"]["width"]
        height = rect["rect"]["height"]
        square_x = rect["rect"]["x"]
        square_y = rect["rect"]["y"]
        if square_x <= mouse_x <= square_x + width and square_y <= mouse_y <= square_y + height:
            collide = rect #Esto guarda todo el rectangulo si ha colisionado
        

# Dibuixar
def app_draw():
    global color, collide
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils1.draw_grid(pygame, screen, 50)
    
    for rect in rectangles:
        width = rect["rect"]["width"]
        height = rect["rect"]["height"]
        square_x = rect["rect"]["x"]
        square_y = rect["rect"]["y"]
        
        """Si en la variable collide se guarda el rectangulo que iteramos, se pintara del color que toca,
        si no se pinta negro"""
        if collide == rect: 
            pygame.draw.rect(screen, rect["color"],(square_x, square_y, width, height))

        pygame.draw.rect(screen, BLACK, (square_x, square_y, width, height),5)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()
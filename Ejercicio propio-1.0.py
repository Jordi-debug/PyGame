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

# Definir les dades
"""dades = [ 
  {'nom': 'Pelut', 'any': 2018, 'pes': 6.5, 'especie': 'Gos'},
  {'nom': 'Pelat', 'any': 2020, 'pes': 5.0, 'especie': 'Gos'},
  {'nom': 'Mia', 'any': 2022, 'pes': 3.0, 'especie': 'Gat'},
  {'nom': 'Nemo', 'any': 2003, 'pes': 0.1, 'especie': 'Peix'},
  {'nom': 'Mickey', 'any': 1928, 'pes': 0.5, 'especie': 'Ratolí'},
  {'nom': 'Donald', 'any': 1934, 'pes': 0.5, 'especie': 'Ànec'} ]

font0 = pygame.font.SysFont("Arial", 18)
font1 = pygame.font.SysFont("Arial", 16)"""
clicked = False
get_big = True #Se inicia en True prque lo primero que vamos haer es aumentar // en False reduiremos
square_x = 0
square_y = 0
width = 50
height = 50
color = BLACK

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
    global black, square_x, square_y, width, height, get_big,color
    mouse_x, mouse_y = pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[0]

    if clicked and square_x <= mouse_x <= square_x + width and square_y <= mouse_y <= square_y + height:
        # Se inicia get_big que es la que controla el crecimiento, mientras este creciendo se dicen las variables que ha de cumplir
        if get_big:
            width += 5
            height += 5
            color = CYAN
            if width >= 640 and height >= 480: #Cuando se cumple esta condición deja de aumentar su tamaño
                get_big = False

        else: #Cuando esta decreciendo
            width -= 5
            height -= 5
            color = SOFT_BLUE
            if width <= 50 and height <= 50: #Cuando ya es lo suficientemente pequeño se inicia de nuevo a true get_big para volver a aumentar su tamaño 
                get_big = True
    else:
        color = GREEN
        
# Dibuixar
def app_draw():
    global black, square_x, square_y, width, height, get_big,color
    
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils1.draw_grid(pygame, screen, 50)

    # Dibuixar el fons de la taula
    pygame.draw.rect(screen, color, (square_x, square_y, width, height))
    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()
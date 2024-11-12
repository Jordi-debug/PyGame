import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
import random

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
PINK = (255, 105, 180)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Bucle de l'aplicació
def main():
    is_looping = True
    window_width, window_height = screen.get_size()
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
        if pygame.mouse.get_pressed()[0] == True:
            print("Left mouse click")
            pos = pygame.mouse.get_pos()
            print(pos)
        if pygame.mouse.get_pressed()[0] == False:
            print("Left mouse release")
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    pass

def draw_polygon(screen, color, center, radius, num_vertices, angle_offset=(math.pi / 3)):
    points = [
        (
            center[0] + radius * math.cos(angle_offset + i * 2 * math.pi / num_vertices),
            center[1] + radius * math.sin(angle_offset + i * 2 * math.pi / num_vertices)
        )
        for i in range(num_vertices)
    ]
    pygame.draw.polygon(screen, color, points)

# Dibuixar
def app_draw():
    dades = [ 
  {'nom': 'Pelut', 'any': 2018, 'pes': 6.5, 'especie': 'Gos'},
  {'nom': 'Pelat', 'any': 2020, 'pes': 5.0, 'especie': 'Gos'},
  {'nom': 'Mia', 'any': 2022, 'pes': 3.0, 'especie': 'Gat'},
  {'nom': 'Nemo', 'any': 2003, 'pes': 0.1, 'especie': 'Peix'},
  {'nom': 'Mickey', 'any': 1928, 'pes': 0.5, 'especie': 'Ratolí'},
  {'nom': 'Mickey', 'any': 1928, 'pes': 0.5, 'especie': 'Ratolí'},
  {'nom': 'Donald', 'any': 1934, 'pes': 0.5, 'especie': 'Ànec'} ]
    
    fontTitol = pygame.font.SysFont("Arial",18)
    fontDetalls = pygame.font.SysFont("Arial",16)
    blau = (50,120,200)
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)
    pygame.draw.rect(screen,WHITE,(150,100,200,150))

    for i in range(0,len(dades)+1):
        pygame.draw.line(screen,BLACK,(150,i),(350,i),2) 

    for pos in range(len(dades)):
        item = dades[pos]
        y = 100 + 25*pos + 2
        textTitol = fontTitol.render(item["nom"],True,BLACK)
        textDetallsAny = fontDetalls.render(str(item["any"]),True,blau)
        textDetallsE = fontDetalls.render(item["especie"],True,blau)
        screen.blit(textTitol,(150,y))
        screen.blit(textDetallsAny,(250,y))
        screen.blit(textDetallsE,(300,y))
        

    


    pygame.display.update()

if __name__ == "__main__":
    main()

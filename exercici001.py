import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (100, 150, 100)
RED = (200, 0, 0)



pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    text = "HEADLINE NEWS"
    font_rect = pygame.font.SysFont("Arial",60)
    text_rect = font_rect.render(text,True,WHITE)

    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)
    #Primer fem el cuadrat
    #Text cuadrat
    pygame.draw.rect(screen, RED, pygame.Rect(50,50,550,100))
    screen.blit(text_rect, (75, 70))
    #Text World
    font_world = pygame.font.SysFont("Courier New",40,bold=True)
    text_world = font_world.render('World goes Wrong!',True,BLACK)
    screen.blit(text_world,(50,160))
    #Text yep buddy
    font_yep = pygame.font.SysFont("Courier New",40,bold=True)
    text_yep = font_yep.render("YEP#",True,(100,150,100))
    screen.blit(text_yep,(500,155))
    #Texto Latin
    font_latin = pygame.font.SysFont("Arial",25)
    text_latin1 = font_latin.render("Lorem ipsum dolor sit amet, consectetur",True,BLACK)
    text_latin2 = font_latin.render("adipiscing elit, sed do eiusmod tempor",True,BLACK)
    text_latin3 = font_latin.render("incididunt ut labore et dolore magna aliqua",True,BLACK)
    screen.blit(text_latin1,(50,250))
    screen.blit(text_latin2,(50,290))
    screen.blit(text_latin3,(50,325))

    pygame.display.update()

if __name__ == "__main__":
    main()
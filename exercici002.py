import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils1

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Bucle de l'aplicació
def main():
    global im_shinnosuke, im_shiro
    is_looping = True

    path_shinnosuke = os.path.join(os.path.dirname(__file__), "./assets/exercici002/shinnosuke.png")
    im_shinnosuke = pygame.image.load(path_shinnosuke).convert_alpha()
    im_shinnosuke = utils1.scale_image(pygame, im_shinnosuke, target_width=100)

    path_shiro = os.path.join(os.path.dirname(__file__), "./assets/exercici002/shiro.png")
    im_shiro = pygame.image.load(path_shiro).convert_alpha()
    im_shiro = utils1.scale_image(pygame, im_shiro, target_width=75)

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
    global im_shinnosuke

    screen.fill(WHITE)
    utils1.draw_grid(pygame, screen, 50)
    
    import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils1

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Bucle de l'aplicació
def main():
    global im_shinnosuke, im_shiro
    is_looping = True

    path_shinnosuke = os.path.join(os.path.dirname(__file__), "./assets/exercici002/shinnosuke.png")
    im_shinnosuke = pygame.image.load(path_shinnosuke).convert_alpha()
    im_shinnosuke = utils1.scale_image(pygame, im_shinnosuke, target_width=100)

    path_shiro = os.path.join(os.path.dirname(__file__), "./assets/exercici002/shiro.png")
    im_shiro = pygame.image.load(path_shiro).convert_alpha()
    im_shiro = utils1.scale_image(pygame, im_shiro, target_width=75)

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
    global im_shinnosuke

    screen.fill(WHITE)
    utils1.draw_grid(pygame, screen, 50)
    
    screen.blit(im_shinnosuke, (325, 165))
    screen.blit(im_shiro, (225, 210))

    pygame.display.update()

if __name__ == "__main__":
    main()

    pygame.display.update()

if __name__ == "__main__":
    main()
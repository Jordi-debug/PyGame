import pygame
import random

# Inicialización de Pygame
pygame.init()

# Configuración de pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Atrapar Objetos")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 128, 255)
OBJECT_COLOR = (255, 0, 0)

# Configuración del jugador
player_size = 50
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT - player_size - 10
player_speed = 7

# Configuración del objeto que cae
object_size = 30
object_x = random.randint(0, SCREEN_WIDTH - object_size)
object_y = 0
object_speed = 5

# Variables de juego
score = 0
lives = 3
font = pygame.font.Font(None, 36)

# Bucle del juego
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_speed

    # Movimiento del objeto
    object_y += object_speed

    # Revisar si el objeto ha sido atrapado
    if (player_x < object_x < player_x + player_size or player_x < object_x + object_size < player_x + player_size) and player_y < object_y + object_size < player_y + player_size:
        score += 1
        # Reiniciar el objeto para que caiga de nuevo desde arriba
        object_x = random.randint(0, SCREEN_WIDTH - object_size)
        object_y = 0
        object_speed += 0.5  # Incrementar la velocidad a medida que se atrapan objetos

    # Revisar si el objeto ha llegado al fondo sin ser atrapado
    elif object_y > SCREEN_HEIGHT:
        lives -= 1
        # Reiniciar el objeto para que caiga de nuevo desde arriba
        object_x = random.randint(0, SCREEN_WIDTH - object_size)
        object_y = 0

    # Dibujar el jugador
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, player_size, player_size))

    # Dibujar el objeto
    pygame.draw.rect(screen, OBJECT_COLOR, (object_x, object_y, object_size, object_size))

    # Mostrar puntuación y vidas
    score_text = font.render("Puntuación: " + str(score), True, BLACK)
    lives_text = font.render("Vidas: " + str(lives), True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))

    # Revisar si el juego ha terminado
    if lives <= 0:
        game_over_text = font.render("Juego Terminado", True, BLACK)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

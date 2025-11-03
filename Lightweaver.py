# Lightweaver: Realm of Solara
# A basic starter framework for your game
# A Game Design by Ella

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lightweaver: Realm of Lightweaver")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)

# Font
font = pygame.font.SysFont("Arial", 36)

# Game states
STATE_MENU = "menu"
STATE_GAME = "game"
game_state = STATE_MENU

# Player
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

# Main game loop
clock = pygame.time.Clock()

def draw_menu():
    screen.fill(LIGHT_BLUE)
    title_text = font.render("Lightweaver: Realm of Lightweaver", True, BLACK)
    start_text = font.render("Press ENTER to Start", True, BLACK)
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, HEIGHT//3))
    screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, HEIGHT//2))
    
def draw_game():
    screen.fill(WHITE)
    pygame.draw.circle(screen, LIGHT_BLUE, player_pos, 25)
    info_text = font.render("Use arrow keys to move", True, BLACK)
    screen.blit(info_text, (20, 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    
    if game_state == STATE_MENU:
        if keys[pygame.K_RETURN]:
            game_state = STATE_GAME
        draw_menu()
    
    elif game_state == STATE_GAME:
        if keys[pygame.K_LEFT]:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT]:
            player_pos[0] += player_speed
        if keys[pygame.K_UP]:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN]:
            player_pos[1] += player_speed
        draw_game()
    
    pygame.display.flip()
    clock.tick(60)

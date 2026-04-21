import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 800
FPS = 60 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Practice 11")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 223, 0)
RED = (255,0,0)

#player param
player_width = 50
player_height = 80

player_x = WIDTH // 2
player_y = HEIGHT - 120
player_speed = 10

#coin param
coins = []
coin_size = 20
coin_spawn_delay = 30
spawn_timer = 0

score = 0 # counter 

enemy_width = 40
enemy_height = 80
enemy_x = random.randint(0, WIDTH - 50)
enemy_y = -100
enemy_speed = 5

level_up_coins = 10

font = pygame.font.Font(None, 36)

def spawn_coin():
    x = random.randint(0, WIDTH - coin_size)
    y = -coin_size
    weight = random.choice([1,2,3]) #diff weightes
    rect = pygame.Rect(x,y,20,20)
    coins.append((rect, weight))

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    player_x = max(0, min(WIDTH - player_width, player_x))

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(0,WIDTH - 50)
        
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
    
    if player_rect.colliderect(enemy_rect):
        running = False

    spawn_timer += 1
    if spawn_timer >= coin_spawn_delay:
        spawn_coin()
        spawn_timer = 0

    for coin in coins[:]:
        rect, weight = coin
        rect.y += 5

        if player_rect.colliderect(rect):
            score += weight #add weight score
            coins.remove(coin)
        elif rect.y > HEIGHT:
            coins.remove(coin)
    
    if score >= level_up_coins:
        enemy_speed = 8
    if score >= level_up_coins*2:
        enemy_speed = 11

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)

    for rect, weight in coins:
        rad = 5 + weight*3
        pygame.draw.circle(screen, YELLOW, rect.center, rad)

    score_text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - 150, 10))

    pygame.display.update()

pygame.quit()
sys.exit()
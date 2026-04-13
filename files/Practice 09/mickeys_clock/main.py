import pygame
import datetime
import os
from clock import rotate_hand

pygame.init()
WIDTH, HEIGHT = 800,800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Mickey's Clock")
clock = pygame.time.Clock()

BASE_PATH = os.path.dirname(__file__)
IMG_PATH = os.path.join(BASE_PATH, 'images')

bg = pygame.image.load(os.path.join(IMG_PATH, 'main-clock.png'))
right_hand_img = pygame.image.load(os.path.join(IMG_PATH, 'right-hand.png'))
left_hand_img = pygame.image.load(os.path.join(IMG_PATH, 'left-hand.png'))

center_pos = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute
    
    minute_angle = minutes*6
    second_angle = seconds*6
    
    screen.blit(bg, (0,0))
    
    min_surf, min_rect = rotate_hand(right_hand_img, minute_angle, center_pos)
    screen.blit(min_surf, min_rect)
    sec_surf, sec_rect = rotate_hand(left_hand_img, second_angle, center_pos)
    screen.blit(sec_surf, sec_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
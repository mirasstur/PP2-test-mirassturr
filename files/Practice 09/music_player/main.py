import pygame 
import os
from player import MusicPlayer

pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Keyboard Music Player")
font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()

MUSIC_FOLDER = os.path.join(os.path.dirname(__file__), 'music')
player = MusicPlayer(MUSIC_FOLDER)

def draw_text(text, x, y, color=(255,255,255)):
    img = font.render(text, True, color)
    screen.blit(img,(x,y))
    
running = True
while running:
    screen.fill((30,30,30))
    draw_text("Music Player Controls:", 50,10,(200,200,200))
    draw_text("[P] Play  [S] Stop  [N] Next  [B] Back  [Q] Quit",50,50)
    
    status = "Playing" if player.is_playing else "Stopped"
    draw_text(f"Status: {status}",50,160,(0,255,0) if player.is_playing else (255,0,0))
    draw_text(f"Current Track : {player.get_current_track_name()}", 50,200)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            
            print(f"Pressed: {pygame.key.name(event.key)}")
            
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q:
                running = False
            
        
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
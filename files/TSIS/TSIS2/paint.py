import pygame
import sys
from datetime import datetime
from tools import flood_fill

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS 2 Paint")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255,255,255))

clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
colors = [
    (0,0,0), (255,0,0), (0,255,0),
    (0,0,255), (255,255,0), (255,165,0)
]

color = BLACK

tool = "pencil"
drawing = False
start_pos = None
last_pos = None

brush_size = 2

font = pygame.font.SysFont("Arial", 20)

text_mode = False
text_pos = None
text_input = ""

def save_canvas():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"canvas_{timestamp}.png"
    pygame.image.save(canvas, filename)
    print("Saved:", filename)
    
def draw_line(surface, start, end,width):
    pygame.draw.line(surface, color, start, end, width)

def draw_shape(surface, start, end, width):
    rect = pygame.Rect(start[0], start[1],
                       end[0] - start[0],
                       end[1] - start[1])
    pygame.draw.rect(surface, color, rect, width)
    
while True:
    screen.fill((200,200,200))
    screen.blit(canvas, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_1:
                brush_size = 2
            if event.key == pygame.K_2:
                brush_size = 5
            if event.key == pygame.K_3:
                brush_size = 10
                
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                save_canvas()
            
            if event.key == pygame.K_p:
                tool = "pencil"
            if event.key == pygame.K_l:
                tool = "line"
            if event.key == pygame.K_r:
                tool = "rect"
            if event.key == pygame.K_f:
                tool = "fiil"
            if event.key == pygame.K_t:
                tool = "text"
                text_input = ""
                text_mode = True
                
            
            if text_mode:
                if event.key == pygame.K_RETURN:
                    if text_pos:
                        text_surface = font.render(text_input, True, color)
                        canvas.blit(text_surface, text_pos)
                    text_mode = False
                    
                elif event.key == pygame.K_ESCAPE:
                    text_mode = False
                    
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1] 
                
                else:
                    text_input += event.unicode  

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            if tool == "fill":
                flood_fill(canvas, x, y, color)
            
            elif tool == "text":
                text_pos = (x,y)
            
            else:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos
                
            for i, col in enumerate(colors):
                rect = pygame.Rect(10 + i*40, 10, 30, 30)
                if rect.collidepoint(event.pos):
                    color = col
                
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                end_pos = event.pos
                
                if tool == "line":
                    draw_line(canvas, start_pos, end_pos, brush_size)
                
                elif tool == "rect":
                    draw_shape(canvas, start_pos, end_pos, brush_size)
                
                drawing = False
            
        if event.type == pygame.MOUSEMOTION:
            if drawing and tool == "pencil":
                pygame.draw.line(canvas, color, last_pos, event.pos, brush_size)
                last_pos = event.pos
                
    
    if drawing and  tool == "line":
        temp = canvas.copy()
        pygame.draw.line(temp, color, start_pos, pygame.mouse.get_pos(), brush_size)
        screen.blit(temp, (0,0))
        
    if text_mode and text_pos:
        preview = font.render(text_input, True, color)
        screen.blit(preview, text_pos)
        
    for i, col in enumerate(colors):
        pygame.draw.rect(screen, col, (10 + i*40, 10, 30, 30))
        
    pygame.display.update()
    clock.tick(60)
    
import pygame
import sys 
import math #----
pygame.init()

width, height = 900,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

colors = [black, red, green, blue]

current_color = black
tool = "brush"

drawing = False
start_pos = (0,0)

screen.fill(white)

def draw_ui():
    for i, color in enumerate(colors):
        pygame.draw.rect(screen, color, (10 + i*40, 10, 30, 30))
    
    pygame.draw.rect(screen, black, (10,60,80,30),2)
    pygame.draw.rect(screen, black, (100, 60, 80, 30), 2)
    pygame.draw.rect(screen, black, (190,60,80,30),2)
    pygame.draw.rect(screen, black, (280,60,80,30), 2)
    pygame.draw.rect(screen, black, (370,60,80,30),2)
    pygame.draw.rect(screen, black, (470, 60, 80, 30), 2)
    pygame.draw.rect(screen, black, (555,60,80,30),2)
    pygame.draw.rect(screen, black, (650,60,80,30), 2)
    
    font = pygame.font.Font(None, 24)
    screen.blit(font.render("Brush", True, black), (15,65))
    screen.blit(font.render("Rect", True, black), (110, 65))
    screen.blit(font.render("Circle", True, black), (200, 65))
    screen.blit(font.render("Eraser", True, black), (285,65))
    
    screen.blit(font.render("Square", True, black), (370,65)) #------
    screen.blit(font.render("R.Triangle", True, black), (470,65))
    screen.blit(font.render("E.Triangle", True, black), (560,65))
    screen.blit(font.render("Romb", True, black), (660,65))

def draw_sq(surface,start,end,color):
    size = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(start[0], start[1], size,size)
    pygame.draw.rect(surface, color, rect, 2)
    
def draw_r_triangle(surface,start,end,color):
    points = [
        start,
        (start[0], end[1]),
        end
    ]
    pygame.draw.polygon(surface, color, points, 2)

def draw_e_triangle(surface,start,end,color):
    side = abs(end[0] - start[0])
    height = int(side * math.sqrt(3) / 2)
    
    p1 = start
    p2 = (start[0] + side, start[1])
    p3 = (start[0] + side//2, start[1] - height)
    
    pygame.draw.polygon(surface, color, [p1,p2,p3], 2)
    
def draw_rh(surface, start, end, color):
    center_x = (start[0] + end[0])//2
    center_y = (start[1] + end[1])//2
    
    dx = abs(end[0] - start[0]) // 2
    dy = abs(end[1] - start[1]) // 2
    
    points = [
        (center_x, center_y - dy),
        (center_x + dx, center_y),
        (center_x, center_y + dy),
        (center_x - dx, center_y)
    ]
    
    pygame.draw.polygon(surface, color, points, 2)
    
canvas = pygame.Surface((width, height))
canvas.fill(white)

running = True

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            
            for i, color in enumerate(colors):
                if pygame.Rect(10 + i*40, 10, 30, 30).collidepoint(x,y):
                    current_color = color
            if pygame.Rect(10,60,80,30).collidepoint(x,y):
                tool = "brush"
            if pygame.Rect(100,60,80,30).collidepoint(x,y):
                tool = "rect"
            if pygame.Rect(190,60,80,30).collidepoint(x,y):
                tool = "circle"
            if pygame.Rect(280,60,80,30).collidepoint(x,y):
                tool = "eraser"
                
            #added--    
            
            if pygame.Rect(370,60,80,30).collidepoint(x,y):
                tool = "square"
            if pygame.Rect(470,60,80,30).collidepoint(x,y):
                tool = "rtri"
            if pygame.Rect(570,60,80,30).collidepoint(x,y):
                tool = "etri"
            if pygame.Rect(660,60,80,30).collidepoint(x,y):
                tool = "rhomb"
                
                
                
            drawing = True
            start_pos = event.pos 
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            
            if tool == "rect":
                rect = pygame.Rect(start_pos,(end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                pygame.draw.rect(canvas, current_color, rect, 2)
                
            if tool == "circle":
                radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
                pygame.draw.circle(canvas,current_color, start_pos, radius, 2)
                
            if tool == "square":
                draw_sq(canvas, start_pos, end_pos, current_color)
            if tool == "rtri":
                draw_r_triangle(canvas, start_pos, end_pos, current_color)
            if tool == "etri":
                draw_e_triangle(canvas, start_pos, end_pos, current_color)
            if tool == "rhomb":
                draw_rh(canvas, start_pos, end_pos, current_color)
                
        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "brush":
                pygame.draw.circle(canvas, current_color, event.pos, 5)
            if tool == "eraser":
                pygame.draw.circle(canvas, white, event.pos, 10)
                
                
    screen.fill(white)
    screen.blit(canvas, (0,0))
    draw_ui()
    
    pygame.display.update()
    
pygame.quit()
sys.exit()
                
                
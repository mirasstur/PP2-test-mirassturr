import pygame 
from collections import deque

def flood_fill(surface, x, y, fill_color):
    width,height = surface.get_size()
    target_color = surface.get_at((x,y))
    
    if target_color == fill_color:
        return
    
    queue = deque()
    queue.append((x,y))
    
    while queue:
        cx,cy = queue.popleft()
        
        if cx < 0 or cy < 0 or cx>=width or cy >= height:
            continue
        if surface.get_at((cx,cy)) != target_color:
            continue
            
        surface.set_at((cx,cy), fill_color)
        
        queue.append((cx+1,cy))
        queue.append((cx-1, cy))
        queue.append((cx, cy + 1))
        queue.append((cx, cy - 1))
        




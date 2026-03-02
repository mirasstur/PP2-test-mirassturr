def duga(Ax, Ay, Bx, By):
    dot = Ax*Bx + Ay*By
    magA = math.hypot(Ax, Ay)
    magB = math.hypot(Bx, By)
    cos_theta = dot / (magA * magB)
    cos_theta = min(1, max(-1, cos_theta))
    theta = math.acos(cos_theta)            
    return theta

import math
R = float(input())
Ax,Ay = map(float,input().split())
Bx,By = map(float,input().split())

dx = Bx - Ax
dy = By - Ay

a = dx**2 + dy**2
b = 2 * (Ax*dx + Ay*dy)
c = Ax**2 + Ay**2 - R**2

D = b**2 - 4*a*c
if D < 0:
    t_st = t_end = None
    res = 0
else:
    sqrtD = math.sqrt(D)
    t1 = (-b - sqrtD) / (2*a)
    t2 = (-b + sqrtD) / (2*a)
    
    t_candidates = [t for t in (t1, t2) if 0 <= t <= 1]
    if not t_candidates:
        t_st = t_end = None
        res = 0
    else:
        t_st = min(t_candidates)
        t_end = max(t_candidates)
        res = 1
        
if res==0:
    AB = math.sqrt(dx**2 + dy**2)
    print(f"{AB:.10f}")
else:
    R1x = Ax + t_st*dx
    R1y = Ay + t_st*dy
    R2x = Ax + t_end*dx
    R2y = Ay + t_end*dy
    
    dx_A_R = Ax - R1x
    dy_A_R = Ay - R1y
    
    dx_B_R = Bx - R2x
    dy_B_R = By - R2y
    
    total_dist = math.sqrt(dx_A_R**2 + dy_A_R**2) + math.sqrt(dx_B_R**2 + dy_B_R**2)
    
    t_deg = duga(R1x,R1y,R2x,R2y)
    
    len_duga = R * t_deg
    total_dist += len_duga
    print(f"{total_dist:.10f}")
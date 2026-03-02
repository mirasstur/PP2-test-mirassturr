import math
R = float(input())
Ax,Ay = map(float,input().split())
Bx,By = map(float,input().split())

dx = Bx - Ax
dy = By - Ay

a = dx**2 + dy**2
b = 2*(Ax * dx + Ay * dy)
c = Ax**2 + Ay**2 - R**2

if a==0:
    print(f"{R if Ax**2 + Ay**2 <= R**2 else 0:.10f}")

else:
    D = b**2 - 4*a*c
    if D < 0:
        dist = 0

    else:
        t1 = (-b + math.sqrt(D)) / (2*a)
        t2 = (-b - math.sqrt(D)) / (2*a)
        
        t_st = max(0, min(t1,t2))
        t_end = min(1, max(t1, t2))
        
        if t_end < t_st:
            dist = 0
        else:
            AB = math.sqrt(dx**2 + dy**2)
            dist = AB * (t_end-t_st)

    print(f"{dist:.10f}")

# if points:
#     (x1, y1),(x2,y2) = points[0], points[-1]
#     print(x1, y1)
#     print(x2, y2)
#     lenz = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# else:
#     lenz = 0
# print(f"{lenz:.10f}")


import json
import re

def solve():
    try:
        data_input = input().strip()
        data = json.loads(data_input)
    except EOFError:
        return

    try:
        num_queries = int(input().strip())
    except EOFError:
        return

    for _ in range(num_queries):
        query = input().strip()
        
        parts = re.findall(r'[^.\[\]]+|\[\d+\]', query)
        
        current = data
        possible = True
        
        for part in parts:
            if part.startswith('[') and part.endswith(']'):
                
                index = int(part[1:-1])
                if isinstance(current, list) and 0 <= index < len(current):
                    current = current[index]
                else:
                    possible = False
                    break
            else:
                
                if isinstance(current, dict) and part in current:
                    current = current[part]
                else:
                    possible = False
                    break
        
        if possible:
            
            print(json.dumps(current, separators=(',', ':'), ensure_ascii=False))
        else:
            print("NOT_FOUND")

if __name__ == "__main__":
    solve()
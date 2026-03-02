xa, ya = map(float,input().split())
xb, yb = map(float, input().split())

xr = xa + ya*((xb - xa)/(ya + yb))
print(f"{xr:.10f} {0:.10f}")
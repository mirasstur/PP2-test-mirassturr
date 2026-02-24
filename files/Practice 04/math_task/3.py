import math
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
area = (1/2) * n * l * (l / (2 * math.tan(math.radians(180)/ n)))
area = round(area)
print(f"The area of the polygon is: {area}")
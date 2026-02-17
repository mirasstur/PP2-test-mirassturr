# class Shape:
#     def __init__(self,len,wid):
#         self.len = len
#         self.wid = wid
# class Rectangle(Shape):
#     def __init__(self,len,wid):
#         Shape.__init__(self,len,wid)
#         self.area = len*wid
    
# t,s = map(int,input().split())
# a = Rectangle(t,s)
# print(a.area)


# 307 
# v v v


# import math

# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def show(self):
#         return (self.x, self.y)
#     def move(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#     def dist(self, ox, oy):
#         self.ox = ox
#         self.oy = oy
#         return math.sqrt((self.ox - self.x)**2  + (self.oy - self.y)**2)
        
# ix, iy = map(int,input().split())
# nx, ny = map(int,input().split())
# dx, dy = map(int,input().split())
# p = Point(ix,iy)
# print(f"({p.x:.0f}, {p.y:.0f})")

# p.move(nx,ny)
# print(f"({p.x:.0f}, {p.y:.0f})")

# print(f"{p.dist(dx,dy):.2f}")


# 308 ------- 
#     V V V V        

# class Accout:
#     def __init__(self,balance):
#         self.balance = balance
#     def deposit(self, amount):
#         if (amount > self.balance):
#             return "Insufficient Funds"
#         else:
#             self.balance -= amount
#             return str(self.balance)

# a,b = map(int,input().split())
# p = Accout(a)
# print(p.deposit(b))


# 309 -----
#     V V V

# import math
# p = math.pi
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self, radius):
#         return (self.radius**2 * p)

# l = int(input())
# c = Circle(l)
# print(f"{c.area(l):.2f}")

# class Person:
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#     def display(self):
#         print(f"Student: {self.name}, GPA: {self.gpa}")
        
# a, b = map(str, input().split())
# p = Person(a, b)
# p.display()

# class Pair:
#     def __init__(self, a1,b1,a2,b2):
#         self.a1 = a1
#         self.b1 = b1
#         self.a2 = a2
#         self.b2 = b2
#     def add(self):
#         print(f"Result: {self.a1 + self.a2} {self.b1 + self.b2}")
# a1,b1,a2,b2 = map(int,input().split())
# p = Pair(a1, b1, a2, b2)
# p.add()

# class Employee:
#     def __init__(self, name, bs):
#         self.name = name
#         self.bs = bs
#     def Mang(self, bp):
#         total = int(self.bs)*(1 + int(bp)/100)
#         print(f"Name: {self.name}, Total: {total:.2f}")
#     def Dev(self, cp):
#         total = int(self.bs) + int(cp)*500
#         print(f"Name: {self.name}, Total: {total:.2f}")
#     def Intr(self):
#         print(f"Name: {self.name}, Total: {int(self.bs):.2f}")

# l = list(map(str,input().split()))
# p = Employee(l[1], l[2])
# if (l[0] == "Manager"):
#     p.Mang(l[3])
# elif (l[0] == "Developer"):
#     p.Dev(l[3])
# elif (l[0] == "Intern"):
#     p.Intr()

# import math
# is_prime = lambda x : x > 1 and all(x%i != 0 for i in range(2, int(math.sqrt(x))+1))
# nums = list(map(int, input().split())) 
# primes = list(filter(is_prime, nums))
# if primes:
#     print(" ".join(map(str, primes)))
# else:
#     print("No primes")

# n = int(input())
# nums = list(map(int,input().split()))
# q = int(input())
# newf = nums
# while(q>0):
#     ops = list(map(str, input().split()))
#     if ops[0] == "abs":
#         newf = list(map(lambda x: abs(x), newf))
#     elif ops[0] == "add":
#         newf = list(map(lambda x: x + int(ops[1]), newf))
#     elif ops[0] == "multiply":
#         newf = list(map(lambda x : x * int(ops[1]), newf))
#     elif ops[0] == "power":
#         newf = list(map(lambda x: x**int(ops[1]), newf))
#     q=q-1
# print(" ".join(map(str,newf)))



class Person:
    def __init__(self,name):
        self.name = name
        
    def greet(self):
        print("Hi, I am " + self.name)
        
p1=Person("Miras")
p1.greet()


class Calc:
    def add(self, a, b):
        return a+b
    def mult(self, a, b):
        return a*b

calcul=Calc()
print(calcul.add(5, 3))
print(calcul.mult(4, 7))
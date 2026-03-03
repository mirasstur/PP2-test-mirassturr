class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lasname = lname
        
class Student(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname)
        self.age = age
        
p = Student("Miras", "Turganbai", 25)
print(p.firstname)
print(p.lasname)
print(p.age)

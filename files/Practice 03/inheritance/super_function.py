class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет.")


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def introduce(self):
        print(f"Я студент {self.university}, меня зовут {self.name}, мне {self.age} лет.")

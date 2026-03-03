class Mother:
    def speak(self):
        print("I am Mom")
        
class Father:
    def speak(self):
        print("I am Dad")
        
class child(Mother, Father):
    pass
c = child()
c.speak()
        
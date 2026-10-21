import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print(self.radius*self.radius*math.pi)

class Square:
    def __init__(self,side):
        self.side=side

    def area(self):
        print(self.side**2)


C1=Circle(10)
S1=Square(25)
C1.area()
S1.area()

class Musaddique:
    def sound(self):
        print("Bhau Bhau")

class Musaddique2:
    def sound(self):
        print("Meow Meow")

D1=Musaddique()
C1=Musaddique2()

D1.sound()
C1.sound()
from abc import ABC,abstractmethod
class Data(ABC):
    def __init__(self,a):
        print("This is a constructor in abstract base class")
        self.a=a**2

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def show(self):
        pass

    def mymethods(self):
        print("Concrete method")

class NewData(Data):
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b**3

    def display(self):
        print("This is the implementation of display Method")

    def show(self):
        print("This is the implementation of show method")
        print(self.a)
        print(self.b)

N1=NewData(2,3)
N1.display()
N1.show()
N1.mymethods()
from abc import ABC, abstractmethod
class Shape(ABC):
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
r=Rectangle(10,20)
print("Area:", r.area())
print("Perimeter:", r.perimeter())

class Student:
    def _init_(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,name):
        self.name = name
    def set_age(self,age):
        self.age = age

name = input("Enter the Name:")
age = int(input("Enter the Age:"))
s = Student(name,age)
print(f"Name:{s.get_name()}\nAge:{s.get_age()}")          

#other method
class Student:
    def _init_(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,name):
        self.name = name
    def set_age(self,age):
        self.age = age

name = input("Enter the Name:")
age = int(input("Enter the Age:"))
s = Student(name,age)
n = input()
s.set_name(n)
print(f"Name:{s.get_name()}\nAge:{s.get_age()}")

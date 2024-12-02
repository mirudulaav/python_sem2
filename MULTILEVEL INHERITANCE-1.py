#1
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age=age
    def displayPerson(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Employee(Person):
    def __init__(self, name, age, ID):
        super().__init__(name,age)
        self.ID=ID
    def displayEmployee(self):
        self.displayPerson()
        print("ID:", self.ID)

class Manager(Employee):
    def __init__(self, name, age, ID, salary):
        super().__init__(name, age, ID)
        self.salary=salary
    def displayManager(self):
        self.displayEmployee()
        print("Salary:", self.salary)

per= Manager("Diana", 35, 100, 20000)
per.displayManager()

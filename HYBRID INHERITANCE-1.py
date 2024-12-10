class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Personinfo(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Employee(Person):
    def __init__(self, name, age, ID):
        super().__init__(name, age)
        self.ID = ID
    def Employeeinfo(self):
        print("Employee ID:", self.ID)

class Salary(Employee):
    def __init__(self, name, age, ID, salary):
        super().__init__(name, age, ID)
        self.salary = salary
    def Salaryinfo(self):
        print(f"Salary: {self.salary}")

class Persondetails(Salary):
    def __init__(self, name, age, ID, salary):
        super().__init__(name, age, ID, salary)
    def displayjob(self):
        self.Personinfo()
        self.Employeeinfo()
        self.Salaryinfo()

emp = Persondetails("Megha", 27, 1877, 30000)
emp.displayjob()
        
        

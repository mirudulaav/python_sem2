#1
class Person:
    def __init__(self, name):
        self.name = name  
    def show_name(self):
        print(f"Name: {self.name}")  

class Student(Person):
    def __init__(self, name, stu_id):
        super().__init__(name)  
        self.stu_id = stu_id  
    def show_student_id(self):
        print(f"Student ID: {self.stu_id}")  
stu= Student("Alice", "S12345")
stu.show_name()       
stu.show_student_id()

#2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.dept = dept
    
    def display_department(self):
        print(f"Department: {self.dept}")
manager = Manager("Megha", 75000, "IT")
manager.display_details()    
manager.display_department()  


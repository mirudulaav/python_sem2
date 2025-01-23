from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department
    def calculate_salary(self):
        pass
    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, department, monthly_salary):
        super().__init__(name, employee_id, department)
        self.monthly_salary= monthly_salary
    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, department, hours, wage):
        super().__init__(name, employee_id, department)
        self.hours=hours
        self.wage=wage
    def calculate_salary(self):
        return self.hours*self.wage

full_time=FullTimeEmployee("Joe", 'E123', "Engineering", 50000)
part_time=PartTimeEmployee("Niki", 'E123', 'Marketing', 200, 80)

print("Full-Time Employee Details:")
full_time.display_details()
print(f"Salary: {full_time.calculate_salary()}")

print("Part-Time Employee Details")
part_time.display_details()
print(f"Salary: {part_time.calculate_salary()}")
           
        
                 
    
    
    

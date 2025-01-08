from abc import ABC, abstractmethod

class Employee(ABC): #Abstract class
    def calculate_pay(self): #Abstract method
        pass

class SalariedEmployee:
    def __init__(self, name, annual_salary):
        self.name=name
        self.annual_salary= annual_salary
    def CalculatePay(self):
        return self.annual_salary/12
        
class HourlyEmployee:
    def __init__(self, name, hoursworked, hourlyrate):
        self.name=name
        self.hoursworked=hoursworked
        self.hourlyrate=hourlyrate
    def CalculatePay(self):
        return self.hourlyrate*self.hoursworked

salary1= SalariedEmployee("John Doe", 5000.00 )
print(f"Salaried Employee {salary1.name} Pay: ${salary1.CalculatePay():.2f}")

salary2= HourlyEmployee("Jane Smith", 20, 120)
print(f"Hourly Employee {salary2.name} Pay: ${salary2.CalculatePay():.2f}")

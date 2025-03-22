class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Monthly Salary: {self.salary}")

    def calculate_yearly_salary(self):
        yearly_salary = self.salary * 12
        return yearly_salary

employee = Employee("John Doe", "E12345", 50000)
employee.display_info()
print(f"Yearly Salary: {employee.calculate_yearly_salary()}")

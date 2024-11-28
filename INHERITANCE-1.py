'''class Student:
    def display(self):
        print("Base class-parent")
class Student_derived(Student):
    def show(self):
        print("Derived class-child")
s =Student_derived()
s.display()
s.show()'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name={self.name}\nAge={self.age}")
class Student(Person):
    def __init__(self,name,age,stu_id,stu_dept):
        super().__init__(name,age)
        self.stu_dept=stu_dept
        self.stu_id=stu_id
    def printDetails(self):
        self.display()
        print(f"ID={self.stu_id}\nDepartment={self.stu_dept}")
s=Student('Geetha',35,1200,'AI')
s.printDetails()

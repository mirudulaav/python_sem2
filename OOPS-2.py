 class Student:
    def __init__(self):
        self.name="Mithran"
        self.dept="AI"
    def display(self):
        print(f"Name={self.name}\nDepartment={self.dept}")
stu=Student()
stu.display()

class Library:
    def __init__(self):
        self.name="It Ends with us"
        self.aname="Collen Hoover"
    def display(self):
        print(f"Book Name={self.name}\nAuthor Name={self.aname}")
lib=Library()
lib.display()

class Student:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
    def display(self):
        print(f"Name={self.name}\nDepartment={self.dept}")
stu=Student("Geetha","AI")
stu.display()

class Student:
    def __init__(self,dept,age= 20,name='Dinesh'):
        self.age=age
        self.name=name
        self.dept=dept
    def display(self):
        print(f"Name={self.name}\nDepartment={self.dept}\nAge={self.age}")
    def __del__(self):
        print(f"Object is destroyed")
stu=Student("AI")
stu.display()
del stu


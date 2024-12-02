class Person:
    def __init__(self, name, age):
        self.name= name
        self.age=age
    def displayPerson(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Student(Person):
    def __init__(self, name, age, admnno):
        super().__init__(name,age)
        self.admnno=admnno
    def displayStudent(self):
        self.displayPerson()
        print("Admn No:", self.admnno)

class StudentInfo(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender=gender
    def displayStudentInfo(self):
        self.displayPerson()
        print("Gender:", self.gender)

stu1= StudentInfo("Diana", 17, "Female")
stu1.displayStudentInfo()
stu2= Student("Miya", 17, 1877)
stu2.displayStudent()

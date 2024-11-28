#1
class Student:
    def _init_(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def get_grade(self):
        percentage = sum(self.marks) / len(self.marks)
        if percentage >= 85:
            print("S")
        elif percentage >= 75:
            print("A")
        elif percentage >= 65:
            print("B")
        elif percentage >= 55:
            print("C")
        elif percentage >= 50:
            print("D")
        else:
            print("F")
            
name = input("Enter the student's name: ")
roll_no = input("Enter the roll number: ")
marks = [float(input(f"Enter marks for subject {i + 1}: ")) for i in range(3)]

stu= Student(name, roll_no, marks)
print(f"Name: {student.name}, Roll Number: {student.roll_no}, Grade: {student.get_grade()}")

#2
class Student:
    def _init_(self, name, age, course, grade):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade
        print(f"Student {self.name} is created.")

    def display_info(self):
        print("\nStudent Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Grade: {self.grade}")

    def _del_(self):
        print(f"Student {self.name}'s data is deleted.")
        
name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))
course = input("Enter the course: ")
grade = input("Enter the grade: ")

student = Student(name, age, course, grade)
student.display_info()
del student

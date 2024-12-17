class Student:
    def __init__(self, name, age, marks):
        self._name = name
        self._age = None
        self._marks = None
        self.set_age(age)
        self.set_marks(marks)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, age):
        if 5 <= age <= 100:
            self._age = age
        else:
            raise ValueError("Age must be between 5 and 100.")

    def get_age(self):
        return self._age

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
        else:
            raise ValueError("Marks must be between 0 and 100.")

    def get_marks(self):
        return self._marks


# Example usage
name = input("Enter the name: ")
age = int(input("Enter the age: "))
marks = int(input("Enter the marks: "))

try:
    student = Student(name, age, marks)
    print(f"\nStudent Name: {student.get_name()}")
    print(f"Student Age: {student.get_age()}")
    print(f"Student Marks: {student.get_marks()}")
except ValueError as e:
    print(e)

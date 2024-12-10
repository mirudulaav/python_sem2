#1
class Camera:
    def __init__(self, resolution):
        self.resolution = resolution
    def photoresolution(self):
        print(f"Photo of resolution {self.resolution}")

class Phone:
    def __init__(self, phoneno):
        self.phoneno = phoneno
    def sendmessage(self, message):
        print(f"Sending message to {self.phoneno}: {message}")

class Smartphone(Camera, Phone):
    def __init__(self, resolution, phoneno, brand, model):
        Camera.__init__(self, resolution)
        Phone.__init__(self, phoneno)
        self.brand = brand
        self.model = model
    def displayDeviceInfo(self):
        print(f"Smartphone Information:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Phone Number: {self.phoneno}")
        print(f"Camera Resolution: {self.resolution}")

smartphone = Smartphone(resolution="50MP", phoneno="1234567899", brand="Samsung", model="Galaxy S23")
smartphone.displayDeviceInfo()
smartphone.sendmessage("Hello")

#2
class Student:
    def __init__(self, name, course):
        self.name= name
        self.course= course
    def displayStudentInfo(self):
        print(f"Name: {self.name}\nCourse: {self.course}")

class StudentAthlete(Student):
    def __init__(self, name, course, sports):
        super().__init__(name, course)
        self.sports= sports
    def displayAthleteInfo(self):
        self.displayStudentInfo()
        print(f"Sports: {self.sports}")

stu1= StudentAthlete("Joe", "Computer Science", "FootBall")
stu1.displayAthleteInfo()


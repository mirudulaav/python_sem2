#1
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end=' ')
        i= i+ (n - j)
    print()

#2
arr = list(map(int, input("Enter space-separated numbers: ").split()))
for num in arr:
    if arr.count(num) > len(arr) // 2:
        print(f"{num} appears more than n/2 times")
        break

#3
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def average_marks(self):
        return sum(self.marks.values()) / len(self.marks)
students = [
    Student("Joe", 21, {"Math": 85, "Science": 90}),
    Student("Niki", 22, {"Math": 78, "Science": 80}),
    Student("XYZ", 23, {"Math": 92, "Science": 95})
]
topper = students[0]
for s in students:
    if s.average_marks() > topper.average_marks():
        topper= s
print(f"Topper: {topper.name}, Roll No: {topper.roll_no}, Average Marks: {topper.average_marks():.2f}")

#4
class Product_Info:
    def __init__(self, name, brand, price, discount):
        self.name=name
        self.brand=brand
        self.price=price
        self.discount=discount
    def discount_price(self):
        if self.discount:
            return (self.price-self.price*self.discount/100)
        else:
            print("No discount available")
    def display_details(self):
        print(f"Laptop Name:{self.name}")
        print(f"Brand Name:{self.brand}")
        print(f"Price: {self.price}")
        print(f"Discount: {self.discount}")
        print(f"Final price after discount: {self.discount_price()}")
pdt1=Product_Info("Laptop", "Dell", 80000, 10)
pdt1.display_details()
    
    

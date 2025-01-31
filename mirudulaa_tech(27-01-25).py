#1
def validate_name(name):
    if name.isalpha():
        return name
def validate_password(password):
    s= "!@#$%^&*"
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in s for char in password)
    if len(password)>=8 and has_digit and has_special:
        return password
def main():
    while True:
        name = input("Enter your Name: ")
        if validate_name(name):
            break
        print("Invalid Name!")
    department = input("Enter your Department: ")
    while True:
        password = input("Enter your Password: ")
        if validate_password(password):
            re_password = input("Re-Type your Password: ")
            if password == re_password:
                break
            else:
                print("Passwords do not match. Please try again.")
        else:
            print("Invalid Password!")
    print(f"Your Encoded Name is: {'X' * len(name)} – Fresher")
    print(f"Your Department is: {'X' * len(department)}")
    print(f"Your Password is: {'X' * len(password)}")
    print(f"Re-Type your Password: {'X' * len(re_password)}")
if __name__ == "__main__":
    main()

#2
import array as arr
a=arr.array('i', [1,2,3,4,5,3])
print('Original Array', a)
a.remove(3)
print('New Array', a)

#3
n = int(input('Enter number of elements: '))
a = []
for i in range(n):
    a.append(input(f"Enter element: "))
print('Non-Inverse Order Array is -', a)
print('Inverse Order Array is -', a[::-1])

    

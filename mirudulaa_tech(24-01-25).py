#1
first_name = "Nisha"
last_name = "Varma"
full_name = first_name + " " + last_name
print("Your Name is:", full_name)

college_name = "XYZ College"
stream = "Department of CSE"
college_details = college_name + " " + stream
print("Your College Name:", college_details)

print("\nASCII value of your Name:") 
for char in full_name:
    print(f"{char}-{ord(char)}")

print("\nASCII value of your Mobile Number:") 
mobile_no=str(int(input()))
for digit in mobile_no:
    print(f"{digit}-{ord(digit)}")

print("\nResult of Addition:")
for i in range(min(len(full_name), len(mobile_no))):
    print(f"{full_name[i]}+{mobile_no[i]} = {ord(full_name[i]) + ord(mobile_no[i])}")

#2
val1= 30
val2= 20
add= val1+val2
sub= val1-val2
multiply= val1* val2
division= val1/ val2
modulus= val1% val2
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", multiply)
print("Division:", division)
print("Modulus:", modulus)

x = 30
y = 20
z = 10
print("\nBefore Swapping")
print("First value:", x)
print("Second value:", y)
print("Third Value:", z)
x = x ^ y
y = x ^ y
x = x ^ y
y = y ^ z
z = y ^ z
y = y ^ z
print("\nAfter Swapping")
print("First value:", x)  
print("Second value:", y)
print("Third value:", z)  

#3
def username(username):
    spl_char=' '
    for char in username:
        if not char.isdigit():
            spl_char+=char
    print(f'Hi! Your Entered Input is "{spl_char}"')
first_name=input("Enter required username:")
username(first_name)

def split_char(name):
    characters = ''
    special_characters = ''
    for char in name:
        if char.isalpha():
            characters += char
        elif not char.isalnum():
            special_characters += char
    print(f"Your entered Characters are – {characters}")
    print(f"Your entered Special Characters are – {special_characters}")
name = input("Enter required name:")
split_char(name)


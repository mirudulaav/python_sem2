#1
def count(s):
    upper_count=0
    lower_count=0
    for i in s:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
    return upper_count,lower_count
string=input("Enter string:")
upper_count,lower_count= count(string)
print(f"Uppercase letter count: {upper_count}")
print(f"Lowercase letter count: {lower_count}")

#2
def count_odd_even(numbers):
    odd_count = 0
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count, even_count

n = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

odd_count, even_count = count_odd_even(numbers)
print(f"Elements in the List: {numbers}")
print(f"Odd count: {odd_count}")
print(f"Even count: {even_count}")

#1
numbers = list(map(int, input().split()))
position = int(input("Enter a number:"))
numbers.sort(reverse=True)
print(numbers[position - 1])

#2
value = int(input())
value_str = str(value)
digit_sum = 0
for idx in range(len(value_str)):
    digit = int(value_str[idx])
    digit_sum += digit ** (idx + 1)
if digit_sum == value:
    print("Yes")
else:
    print("No")

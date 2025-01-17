#QUESTION1--to move zeroes back
array = list(map(int, input("Enter digits").split()))
result = []
for num in array:
    if num != 0:
        result.append(num)
zeros_count = array.count(0)
result.extend([0] * zeros_count)
print("Array after moving zeros to the last:", result)

#QUESTION2--to move zeroes front
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input()))
zero_index = 0
for i in range(len(arr)):
    if arr[i] == 0:
        arr[zero_index], arr[i] = arr[i], arr[zero_index]
        zero_index += 1
print("Updated array:", arr)

#QUESTION3--to calculate the price difference between consecutive elements in an array.
n = int(input("Enter the number of elements in the array: "))
arr = []
price = 0
to calculate the price difference between consecutive elements in an array.for i in range(n):
    e = int(input("Enter the elements: "))
    arr.append(e)
length = len(arr)
for i in range(1, length):
    if arr[i] > arr[i-1]:
        price += arr[i] - arr[i-1]
print("Total price difference:", price)

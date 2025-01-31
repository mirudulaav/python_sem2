#1
a = ['Face', 'Learnz', 'Tech', 'Source', 'Solutions']
print("The Array is:")
for i in range(len(a)):
    print(a[i], '-', 'The Index number is:', i)

#2
a= ['Face', 'Learnz', 'Tech', 'Source', 'Solutions']
a.pop(4)
print('Array after removing an element', a)

#3
a = ['Face', 'Learnz', 'Tech', 'Source', 'Solutions']
a.insert(2, 'Global')
print('Array after adding an element:', a)

#4
a = ['Face', 'Learnz', 'Tech', 'Source', 'Solutions']
print("The Array is:")
for i in range(len(a)):
    print(a[i], '-', 'The Index of array is:', i)

print("\nEven position array:")
for i in range(len(a)):
    if i%2==0:
        print(a[i], '-', 'The Index of array is:', i)

print("\nOdd position array:")
for i in range(len(a)):
    if i%2!=0:
        print(a[i], '-', 'The Index of array is:', i)


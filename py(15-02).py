n=int(input())
list1=[]
for i in range(n):
    num=int(input())
    list1.append(num)
odd=0
even=0
for i in list1:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even count:", even)
print("Odd count:", odd)

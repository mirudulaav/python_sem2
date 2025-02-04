#lambda arguements: expression
'''
add=lambda a,b: a+b
print(add(1,2))

#square each element in the list
L1=list(map(int,input().split()))
square=map(lambda x:x**2, L1)
print(f"Square of numbers: {list(square)}")

#filter even num in a list
L2=list(map(int,input().split()))
even=filter(lambda x:x%2==0, L2)
print(f"Even Numbers: {list(even)}")

t=[(1,2),(2,3),(4,1)]
t1=sorted(t, key=lambda x:x[0]) #x[0]-->based on 1st element in tuple; x[1] --> based on 2nd element in tuple
print(t1)
'''
Name=["mir", "resh", "vin"]
Salary=[20000, 40000, 10000]
phn_no=[1234, 4567, 7890]
S=zip(Name, Salary, phn_no)
sort=sorted(S, key=lambda x:x[1])
print(sort)

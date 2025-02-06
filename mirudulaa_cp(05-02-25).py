#1--(05-02-25)
def sum_prime_num(prime):
    total=0
    for num in prime:
        if num<2:
            flag=False
        else:
            flag=True
            for i in range(2,num):
                if num%i==0:
                    flag=False
                    break
            if flag:
                total+=num
    print("Sum of prime numbers is:", total)
numbers=list(map(int,input("Enter a number by space separated:").split()))
sum_of_prime=sum_prime_num(numbers)

#2--(06-02-25)
def is_prime(p):
    if p==2:
        return True
    if p<2:
        return False        
    for i in range(2,p):
        if p%i==0:
            return False
        return True
def SumDigits(num):
    total=0
    for i in str(num):
        if is_prime(int(i)): #function call
            total+=int(i)
    return total
n=int(input())
result=SumDigits(n)
print(result)
        
        
              

n = int(input("Enter an integer n: "))
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if j == i or j == (2 * n - i):  
            print(i, end="")  
        else:
            print(" ", end="")  
    print()  

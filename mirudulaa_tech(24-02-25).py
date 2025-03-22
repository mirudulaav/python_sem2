def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
start = int(input())
end = int(input())
twin_primes = []
for num in range(start, end):
    if is_prime(num) and is_prime(num + 2):
        twin_primes.append((num, num + 2))
print("Twin Primes:", twin_primes)

import math
def prime(n):
    limit = math.floor(math.sqrt(n))
    for i in range(2,limit+1):
        if n % i == 0:
            return prime(n+1)
    return n

X = int(input())

print(prime(X))

from math import sqrt
def isPrime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    i, xx = 3, int(sqrt(x))
    while i <= xx:
        if x % i == 0:
            return False
        i = i + 2
    return True

N = int(input())
print(sum([1 for _ in range(N) if isPrime(int(input()))]))
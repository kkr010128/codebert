import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

N = int(input())
nums = [int(input()) for i in range(N)]
print(sum([isPrime(n) for n in nums]))
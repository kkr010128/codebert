import sys
from math import *
readline = sys.stdin.readline
def isPrime(x):
    if x == 2 or x == 3:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return False
    s = ceil(sqrt(x))
    for i in range(5, s + 1, 2):
        if x % i == 0:
            return False
    return True
print(sum(isPrime(int(readline())) for _ in range(int(input()))))


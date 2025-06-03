import sys
import math

def isprime(n):
    if n == 2:
        return 1
    if n < 2 or n % 2 == 0:
        return 0

    i = 3
    while i <= math.sqrt(n):
        if n % i == 0:
            return 0
        i += 2
    return 1

n = int(input())
p = 0
for i in map(int, sys.stdin.readlines()):
    p += isprime(i)

print(p)
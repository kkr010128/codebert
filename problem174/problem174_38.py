import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


total = 0
N = int(input())
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            total += gcd(i, j, k)

print(total)

import math
from functools import reduce
K = int(input())

def gcd(*numbers):
    return reduce(math.gcd, numbers)

out = 0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            out += gcd(a,b,c)

print(out)

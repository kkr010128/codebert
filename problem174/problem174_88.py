import math
from functools import reduce

n = int(input())
ans = 0

def gcd(*numbers):
    return reduce(math.gcd, numbers)

for x in range(n):
    for k in range(n):
        for l in range(n):
            ans += gcd(x+1,k+1,l+1)

print(ans)
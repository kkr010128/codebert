a, b = map(int, input().split())
import fractions
g = fractions.gcd(a, b)

if g == 1:
    print(1)
    exit()

import math
def factorize(n):
    d = {}
    temp = int(math.sqrt(n))+1
    for i in range(2, temp):
        while n%i== 0:
            n //= i
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    if d == {}:
        d[n] = 1
    else:
        if n in d:
            d[n] += 1
        elif n != 1:
            d[n] =1
    return d

d = factorize(g)
print(len(d)+1)

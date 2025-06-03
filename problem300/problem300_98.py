import fractions
import math

def primefac(n):
    ret = []
    e = 0
    for i in range(2, math.floor(n**(1/2)) + 1):
        if n % i == 0:
            e = 0
            while n % i == 0:
                e += 1
                n //= i
            ret.append((i, e))
    if n != 1:
        ret.append((n, 1))
    return ret

A, B = map(int, input().split())
c = fractions.gcd(A, B)
print(len(primefac(c))+1)
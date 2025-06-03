import os, sys, re, math
from functools import reduce

def lcm(vals):
    return reduce((lambda x, y: (x * y) // math.gcd(x, y)), vals, 1)

(A, B) = [int(n) for n in input().split()]
print(lcm([A, B]))

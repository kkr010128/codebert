from math import gcd
from itertools import product
N = int(input())
print(sum(gcd(gcd(a,b),c) for a, b, c in product(range(1,N+1), repeat=3)))
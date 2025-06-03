from operator import mul
from functools import reduce

def comb(n, r):
    if n<r:
        return 0
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

N,M=map(int,input().split())
# odd+odd
odd_odd = comb(M,2)
# even+even
even_even = comb(N,2)

print(odd_odd+even_even)
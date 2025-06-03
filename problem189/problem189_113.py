from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n,m = map(int,input().split())

cmb_n = cmb(n,2) if n>=2 else 0
cmb_m = cmb(m,2) if m>=2 else 0

print(cmb_n+cmb_m)
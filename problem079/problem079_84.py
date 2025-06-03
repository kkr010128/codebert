from sys import stdin

input = stdin.readline
import math
from functools import lru_cache
MOD = 10**9 + 7

@lru_cache(None)
def fac(n):
    return math.factorial(n)


def comb(k,n):
    return fac(n)//fac(k)//fac(n-k)

def solve():
    s = int(input())
    if s < 3:
        print(0)
        return
    maxn = s // 3
    res = 0
    for i in range(1,s//3 + 1):
        res += (comb(i-1,s-2*i-1))%MOD
    print(res%MOD)

if __name__ == '__main__':
    solve()

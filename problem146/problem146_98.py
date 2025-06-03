#!python3

import sys
from collections import defaultdict
from math import gcd

iim = lambda: map(int, input().rstrip().split())

def resolve():
    N = input()
    it = map(int, sys.stdin.read().split())
    mod = 10**9 + 7

    d1 = [defaultdict(int), defaultdict(int)]
    z0 = 0
    for ai, bi in zip(it, it):
        if ai == 0 and bi == 0:
            z0 += 1
            continue

        ci = gcd(ai, bi)
        ai, bi = ai // ci, bi // ci

        t = ai * bi < 0
        if ai < 0:
            ai, bi = -ai ,-bi
        elif ai == 0:
            bi = -1
            t = 1

        d1[t][(ai, bi)] += 1


    a1, a2 = d1
    ans = 1
    z1 = 0
    for (ai, bi), v in a1.items():
        k2 = (bi, -ai)
        if k2 in a2:
            v2 = a2[k2]
            ans *= pow(2, v, mod) + pow(2, v2, mod) - 1
            ans %= mod
        else:
            z1 += v

    for (ai, bi), v in a2.items():
        k2 = (-bi, ai)

        if k2 in a1: continue

        z1 += v
    ans *= pow(2, z1, mod)

    print((ans-1+z0) % mod)



if __name__ == "__main__":
    resolve()

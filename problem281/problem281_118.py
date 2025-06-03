#!/usr/bin/env python3
from functools import reduce

x, y = map(int, input().split())

mod = 10**9 + 7


def cmb(n, r, m):
    def mul(a, b):
        return a * b % m

    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return (over * pow(under, m - 2, m))%m


r = abs(x - y)
l = (min(x, y) - r) // 3
r += l
if (x+y)%3 < 1 and l >= 0:
    print(cmb(r + l, l, mod))
else:
    print(0)

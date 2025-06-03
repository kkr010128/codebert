import math
import collections
import fractions
import itertools
import functools
import operator
import bisect

S = int(input())

def ncr(n, r):
    if n < r: return 0
    r = min(r, n-r)
    if r == 0: return 1
    numer = functools.reduce(operator.mul, range(n, n-r, -1), 1)
    denom = functools.reduce(operator.mul, range(1, r+1), 1)
    return numer // denom

def solve():
    mod = 10**9+7
    ans = 0
    for i in range(1, S):
        if 3 * i > S:
            break
        ans += ncr(S-3*i+i-1, i-1)
    ans %= mod
    print(ans)
    return 0

if __name__ == "__main__":
    solve()

import os
from functools import lru_cache

import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

N, M = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))


@lru_cache(maxsize=None)
def solve(n):
    if n == 0:
        return 0
    if n < 0:
        return IINF
    ret = IINF
    for c in C:
        ret = min(ret, solve(n - c) + 1)
    return ret


print(solve(N))


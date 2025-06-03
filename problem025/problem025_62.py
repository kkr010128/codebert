from sys import stdin, stderr
from functools import lru_cache

@lru_cache(maxsize=None)
def rec(i, m):
    if i == 0:
        return m == 0 or A[i] == m

    return rec(i - 1, m) or rec(i - 1, m - A[i])

n = int(input())
A = [int(i) for i in input().split()]
q = int(input())
M = [int(i) for i in input().split()]

for m in M:
    if rec(n - 1, m):
        print('yes')
    else:
        print('no')
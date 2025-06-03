from sys import stdin
import numpy as np
from numba import njit, i8
n, k = map(int, stdin.readline().split())
a = np.array(stdin.readline().split(), dtype = np.int64)

@njit(cache=True)
def c(x, a):
    res = 0
    for i in range(n):
        res += 0 - - a[i] // x - 1
    return res <= k

ng = 0
ok = 10 ** 9 + 1
while ok - ng > 1:
    mid = (ok + ng) >> 1
    if c(mid, a):
        ok = mid
    else:
        ng = mid
print(ok)

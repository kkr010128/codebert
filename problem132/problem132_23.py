import numpy as np
from numba import njit


n, k = map(int, input().split())
a = np.array(list(map(int, input().split())))
@njit('(i8[::1]),', cache=True)
def update(a):
    b = np.zeros_like(a)
    for i, x in enumerate(a):
        l = max(0, i - x)
        r = min(n - 1, i + x)
        b[l] += 1
        if r + 1 < n:
            b[r + 1] -= 1
    b = np.cumsum(b)
    return b
k = min(k, 100)
for i in range(k):
    a = update(a)
print(' '.join(a.astype(str)))

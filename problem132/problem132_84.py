import numpy as np
from numba import jit
n, k = map(int, input().split())
a = np.array(list(map(int, input().split())))
@jit
def imos(a):
    tmp = np.zeros(n+1, dtype=np.int64)
    for i in range(n):
        tmp[max(0, i - a[i])] += 1
        tmp[min(i + a[i] + 1, n)] -= 1
    tmp = np.cumsum(tmp)
    return tmp[:n]

for j in range(1, min(k+1, 50)):
    a = imos(a)
print(*a)
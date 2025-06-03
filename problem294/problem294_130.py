import numpy as np
from numba import njit
 

@njit
def f(a):
    n = len(a)
    cnt = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[k] < a[i] + a[j]:
                    cnt += 1
    return cnt


n = int(input())
a = np.array(input().split(), dtype=np.int32)
a.sort()
print(f(a))

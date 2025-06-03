
import numpy as np
from numba import njit

import math

n,k = map(int,input().split())
a = np.array(input().split(),np.int64)

@njit
def solve(n,k,a):
    for i in range(k):
        new = np.zeros_like(a)
        for j in range(n):
            distance = j - a[j]
            if distance < 0:
                distance = 0
            last =  j + a[j]
            if last > n-1:
                last = n-1
            new[distance]+=1
            if last+1 < n:
                new[last+1]-=1
        a = np.cumsum(new)
        if np.all(a==n):
            break
    return a

a = solve(n,k,a)
print(" ".join(a.astype(str)))
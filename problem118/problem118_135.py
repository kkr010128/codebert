from numba import njit
import numpy as np
@njit("i8(i8,i8,i8[:])")

def f(n,ans,l):
    for i in range(2,n+1):
        for j in range(i,n+1,i):
            l[j] += 1

        ans += (l[i]*i)
    return ans

n = int(input())
l = [1]*(n+1)
l[0] = 0
ans = l[1]
l_np = np.array(l,dtype="i8")

print(f(n,ans,l_np))

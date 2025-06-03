from numba import jit
import numpy as np
n=10**7
@jit("i8[:](i8)")
def Make(n):
    return np.array([i for i in range(n)])
@jit ("i8(i8[:])")
def f(a):
    mod=10**9+7
    ans=0
    for i in a:
        ans+=i
        ans%=mod
    return ans
k=Make(n)
f(k)
a,b=map(int,input().split())
print(a*b)
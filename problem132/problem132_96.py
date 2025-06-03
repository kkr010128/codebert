import numpy as np
from numba import jit

@jit('i4[:](i4,i4,i4[:])',cache = True)
def solve(n,k,A):
    l,r=0,0
    for i in range(k):
        B=np.zeros(n+1,dtype=np.int64)
        for x,y in enumerate(list(A)):
            l=max(0,x-y)
            r=min(n,x+y+1)
            B[l]+=1
            B[r]-=1
        A=np.cumsum(B[:-1])
        if A[A==n].size==n:
            break
    return A
n,k=map(int,input().split())
a=list(map(int,input().split()))
A=np.array(a)
X=solve(n,k,A)
print(*X,sep=' ')
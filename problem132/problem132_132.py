import numpy as np
from numba import jit
@jit(cache=True)
def solve(n,k,A):
    l,r=0,0
    for ki in range(k):
        B=np.zeros(n+1,dtype=np.int64)
        for i,j in enumerate(A):
            l=max(0,i-j)
            r=min(n,i+j+1)
            B[l]+=1
            B[r]-=1
        A=np.cumsum(B[:-1])
        if A[A==n].size==n:
            break
    return A

n,k=map(int,input().split())
A=list(map(int,input().split()))
A=np.array(A)
x=solve(n,k,A)
print(*x)
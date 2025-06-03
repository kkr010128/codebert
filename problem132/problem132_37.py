import numpy as np
from numba import njit
import itertools

@njit
def imos(N,K,A):

    
    B=np.zeros((N+1),dtype=np.int64)
    #B=np.zeros((N+1))
    for i in range(N):
        a=A[i]
        start=max(0,i-a)
        end=min(N,i+a+1)
        B[start]+=1
        B[end]-=1
        #B=np.array(B)
    return np.cumsum(B)[:N]
    

if __name__=="__main__":
    N,K=map(int, input().split())
    A=list(map(int, input().split()))
    for _ in range(K):
        A=imos(N,K,A)
        if A.min()==N:
            break   
    
    print(*A)
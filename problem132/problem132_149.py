import numpy as np
from numba import njit

@njit #処理の並列化
def imos(n,k,a):
    
    l=np.zeros((n+1),dtype=np.int64)
    for i in range(n):
        ai=a[i]
        start=max(0,i-ai) #StartIndex
        end=min(n,i+ai+1) #EndIndex + 1
        l[start]+=1
        l[end]-=1
    return np.cumsum(l)[:n]

if __name__=="__main__":
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    for _ in range(k):
        a=imos(n,k,a)
        if a.min()==n:
            break   
    
    print(*a)

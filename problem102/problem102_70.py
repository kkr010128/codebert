import numpy as np
N, K = map(int,input().split())
A = tuple(map(int,input().split()))
for p in range(1,N-K+1):
    if A[K+p-1] > A[p-1]:
        print("Yes")
    else:
        print("No")
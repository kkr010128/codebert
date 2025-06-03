import numpy as np

N,K=map(int, input().split())
A=np.array(list(map(int, input().split())))

for i in range(K,N):
    if A[i]/A[i-K]>1:
        print('Yes')
    else:
        print('No')

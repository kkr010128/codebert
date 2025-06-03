import numpy as np
import itertools

N = int(input())
info = []
for i in range(N):
    A = int(input())
    for _ in range(A):
        x,y = map(int,input().split())
        info.append((i,x-1,y))
        
A = np.array(list(itertools.product([0,1],repeat=N)),np.bool)
for i,x,y in info:
    bl = (~A[:,i]) | (A[:,x] == bool(y))
    A = A[bl]
 
answer = A.sum(axis = 1).max()
print(answer)

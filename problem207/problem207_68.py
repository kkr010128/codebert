import numpy as np
A=[]
for i in range(3):
    A.append(list(map(int,input().split())))
A=np.array(A)

n=int(input())
for i in range(n):
    b=int(input())
    if b in A:
        A=np.where(A==b,0,A)
cross=0
if A[0][0]+A[1][1]+A[2][2]==0 or A[2][0]+A[1][1]+A[0][2]==0:
    cross=1
print("NYoe s"[0 in np.sum(A,axis=0) or 0 in np.sum(A,axis=1) or cross ::2])
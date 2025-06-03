import numpy as np
N=int(input())
A=input().split()
n=np.zeros(N)

for i in range(N-1):
  n[int(A[i])-1]+=1
for l in n :
  print(int(l))
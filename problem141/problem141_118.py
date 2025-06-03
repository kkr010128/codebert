import numpy as np
N=int(input())
A=np.array(list(map(int,input().split())))
B=np.sum(A)-np.cumsum(np.append(0, A[:len(A)-1]))
v=0
k=0
for i in range(N+1):
  if i==0:
    if N==0 and A[0]==1:
      k=1
    elif A[0]==0:
      k=1
    else:
      print(-1)
      break
  elif i==N:
    if B[i]<=2*(k-A[i-1]):
      k=B[i]
    else:
      k=0
      print(-1)
      break
  else:
    k=min(2*(k-A[i-1]),B[i])
    if k<=0:
      print(-1)
      break
  v+=k
if k>0:
  print(v)
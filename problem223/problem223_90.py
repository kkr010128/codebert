import numpy as np
N,K=map(int,input().split())
a = np.array([int(x) for x in input().split()])
val=sum(a[:K])
max_val=val
for i in range(N-K):
  val+=a[K+i]
  val-=a[i]
  max_val=max(val,max_val)
print(max_val/2+K*0.5)
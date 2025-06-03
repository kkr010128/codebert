import numpy as np
n,k = map(int,input().split())
m = 10**9 + 7
gcds = np.zeros(k+1, int)
ans = 0

for i in range(k,0,-1):
  tmp = pow(k//i,n, m)
  for j in range(i*2,k+1,i):
    tmp -= gcds[j]
  ans = (ans + tmp*i)%m
  gcds[i] = tmp
print(ans)
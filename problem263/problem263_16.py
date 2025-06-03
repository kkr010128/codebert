import numpy as np

n = int(input())
a = list(map(int,input().split()))
a = np.array(a,dtype=np.int64)
point = 0
mod = 10**9+7

b = [((a>>i)&1).sum() for i in range(61)]
c = [n-b[i] for i in range(61)]
d = [c[i]*b[i]%mod for i in range(61)]

point = 0
now = 1

for i in range(61):
    point += now*d[i]
    point %= mod
    now *= 2
    now %= mod

print(point)
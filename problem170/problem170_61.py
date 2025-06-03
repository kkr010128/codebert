import numpy as np

MOD = 10**9 + 7

N,K = map(int, input().split())
k = np.arange(K,N+2)
low = (k-1)*k//2
high = (N-k+1)*k + low + 1
ans = (high-low)%MOD
print(ans.sum()%MOD)
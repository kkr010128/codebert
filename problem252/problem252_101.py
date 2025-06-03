import sys
input = sys.stdin.readline
import numpy as np
N, M = map(int, input().split())
L = list(map(int, input().split()))
A = np.zeros(1<<18)
for i in L:
  A[i] += 1
C = (np.fft.irfft(np.fft.rfft(A) * np.fft.rfft(A)) + .5).astype(np.int64)
G = C.cumsum()
count = np.searchsorted(G, N*N-M)
rest = N*N-M - G[count-1]
temp = (C[:count]*np.arange(count, dtype=np.int64)).sum() + count*rest
ans = sum(L)*2*N - temp
print(ans)
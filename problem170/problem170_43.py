import sys 
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
mod = 10 ** 9 +7
N, K = map(int, readline().split())
# s = [0] * (N+1)
# g = [0] * (N+1)
# g[0] = N % mod
# for i in range(1,N+1):
#     s[i] += (s[i-1] + i ) % mod
#     g[i] += (g[i-1] + N - i) % mod
# ans = (sum(g[K-1:]) % mod  - sum(s[K-1:]) % mod + N-K+2) % mod
# print(ans)
k = np.arange(K,N+2,dtype = np.int64)
low = k*(k-1)//2
high = k*(2*N - k + 1) //2
cnt = high-low+1
print(sum(cnt)%mod)
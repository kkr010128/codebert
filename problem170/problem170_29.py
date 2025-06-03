from itertools import accumulate
N, K = map(int, input().split())
MOD = 10**9 + 7
cum = list(accumulate([0]+ list(range(N+1))))
print((sum(cum[N+1] - cum[N+1-k] - cum[k] + 1 for k in range(K,N+2)))%MOD)
from itertools import accumulate
N, K = map(int, input().split())
P = tuple(accumulate(map(int, input().split())))
ans = P[K - 1]
for i in range(N - K):
  ans = max(P[i + K] - P[i], ans)
print((ans + K) / 2)
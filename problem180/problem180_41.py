N, K = list(map(int, input().split()))
if N >= K:
  N = N % K
print(min(N, max(N-K, K-N)))
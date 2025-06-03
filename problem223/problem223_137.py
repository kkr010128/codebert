N, K = list(map(int, input().split()))
P = list(map(int, input().split()))
s = sum(P[:K])
ans = s
for i in range(N-K):
  s = s - P[i] + P[i+K]  
  ans = max(ans,s)
print((ans + K) / 2)
N, K = map(int, input().split())
P = list(map(int, input().split()))

score = sum(P[:K])
mmax = score
idx = 0
for i in range(1, N-K+1):
  score = score - P[i-1] + P[i+K-1]
  if score > mmax:
    mmax = score
    idx = i
  else:
    continue

print((K+mmax)/2)
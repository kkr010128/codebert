N, M, K = map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

Asum=[0]
Bsum=[0]
for i, a in enumerate(A):
  Asum.append(Asum[i]+a)
for i, b in enumerate(B):
  Bsum.append(Bsum[i]+b)

ans, b = 0, M
for a, asum in enumerate(Asum):
  if asum > K:
    break
  while Bsum[b]>K - asum:
    b-=1
  ans = max(ans, a+b)
print(ans)
 

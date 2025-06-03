N, K = map(int,input().split())
P = [0]+list(map(int,input().split()))
for i in range(1,N+1):
  p = P[i]
  p = (1+p)/2
  P[i] = p+P[i-1]
ans = 0
for i in range(N-K+1):
  ans = max(ans,P[i+K]-P[i])
print(ans)
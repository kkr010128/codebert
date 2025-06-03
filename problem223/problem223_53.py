N,K=list(map(int, input().split()))
P=list(map(int, input().split()))
L=[0]*(N+1)
ans=[0]*(N-K+1)
for i in range(N):
  L[i+1]=(P[i]+1)/2 + L[i]
for j in range(N-K+1):
  ans[j]=L[j+K]-L[j]
print(max(ans))
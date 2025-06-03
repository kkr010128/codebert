N,K=list(map(int, input().split()))
A=list(map(int, input().split()))
ans=[None]*(N-K)
for i in range(N-K):
  if A[K+i]>A[i]:
    ans[i]='Yes'
  else:
    ans[i]='No'
print(*ans, sep='\n')
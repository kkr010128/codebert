N,K=map(int,input().split())
H=list(map(int,input().split()))
H.sort()
ans=0
if N-K>0:
  for x in range(N-K):
    ans += H[x]
print(ans)
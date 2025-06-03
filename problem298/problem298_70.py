N,K=map(int,input().split())
H=list(map(int,input().split()))

ans=0
for i in range(N):
  ans+=H[i]>=K
  
print(ans)
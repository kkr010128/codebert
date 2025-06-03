N,T=map(int,input().split())
L=[]
for i in range(N):
  a,b=map(int,input().split())
  L.append((a,b))
L.sort()

DP=[[0 for i in range(T)] for j in range(N+1)]

for i in range(1,N+1):
  for j in range(T):
    if i>0 and j-L[i-1][0]>=0:
      DP[i][j]=max(DP[i-1][j-L[i-1][0]]+L[i-1][1],DP[i-1][j])
    else:
      DP[i][j]=DP[i-1][j]
ans=0
for i in range(N+1):
  if i!=N:
    ans=max(ans,DP[i][T-1]+L[i][1])
  else:
    ans=max(ans,DP[i][T-1])

print(ans)
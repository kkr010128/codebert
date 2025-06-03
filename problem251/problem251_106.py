N,K=map(int,input().split())
R,S,P=map(int,input().split())
T=input()
dp=[0]*N
data={'r':P,'s':R,'p':S}
ans=0
for i in range(N):
  if 0<=i-K:
    if T[i-K]==T[i]:
      if dp[i-K]==0:
        ans+=data[T[i]]
        dp[i]=1
    else:
      ans+=data[T[i]]
      dp[i]=1
  else:
    dp[i]=1
    ans+=data[T[i]]
print(ans)
N,T = map(int,input().split())
tlist=[0]*N
vlist=[0]*N
tvlist=[[0,0]]*N
dp=[[0]*T for i in range(N+1)]

for i in range(N):
    tvlist[i] = list(map(int,input().split()))
tvlist.sort(key=lambda x: x[0])
for i in range(N):
    tlist[i] = tvlist[i][0]
    vlist[i] = tvlist[i][1]

for i in range(N):
    for t in range(T):
        if t>=tlist[i]:
            dp[i+1][t] = max(dp[i][t],dp[i][t-tlist[i]]+vlist[i])
        else:
            dp[i+1][t] = dp[i][t]

ans=0
for i in range(N):
    ans = max(ans,dp[i][T-1]+vlist[i])

print(ans)
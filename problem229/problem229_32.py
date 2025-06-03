# ABC153 E Crested Ibis vs Monster
f=lambda:map(int,input().split())
H,N=f()
# dp[n][h]:=nthまでで体力をh削るときの最小魔力
INF=10**9
dp=[[INF]*(H+1) for _ in [0]*(N+1)]

for i in range(N+1):
    if i!=0:
        a,b=f()
    else:
        a,b=0,0
    for j in range(H+1):
        if i==0:
            if j==0:
                dp[i][j]=0
            else:
                dp[i][j]=INF
        else:
            dp[i][j]=min(dp[i-1][j],dp[i][max(j-a,0)]+b)

print(dp[N][H]) 
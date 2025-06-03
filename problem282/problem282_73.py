N,T = map(int,input().split())
A = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:x[0])
A.insert(0,[-1,-1])
dp = [[0 for _ in range(T+1)] for _ in range(N)]
for i in range(1,N):
    for j in range(1,T+1):
        dp[i][j] = dp[i-1][j]
        if j>A[i][0]:
            dp[i][j] = max(dp[i][j],dp[i-1][j-A[i][0]]+A[i][1])
dmax = 0
for i in range(1,N+1):
    dmax = max(dmax,dp[i-1][T]+A[i][1])
print(dmax)
#dp[n][t]=max(dp[n-1][t],dp[n-1][t-A[n]]+B[n])
#dp[0][t]=0, dp[n][0]=0,0<=t<=T+max(B)-1, 0<=n<=N
def solve():
    N, T = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    X.sort()
    dp = [[0]*(T+3000) for _ in range(N+1)]
    for n in range(1,N+1):
        for t in range(1,T+X[n-1][0]):
            dp[n][t]=dp[n-1][t]
            if t>=X[n-1][0]:
                dp[n][t]=max(dp[n][t],dp[n-1][t-X[n-1][0]]+X[n-1][1])
    ans = max(dp[N])
    return ans
print(solve())
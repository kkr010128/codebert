N,S = map(int,input().split())
A = list(map(int,input().split()))

mod = 998244353

dp = [[0]*(S+1) for _ in range(N)]

dp[0][0] = 2
if A[0] <= S:
    dp[0][A[0]] = 1

for i in range(1,N):
    for j in range(S+1):
        if j-A[i] >= 0:
            dp[i][j] = dp[i-1][j-A[i]] + 2*dp[i-1][j]
        else:
            dp[i][j] = 2*dp[i-1][j]
        dp[i][j] %= mod

#print(dp)
print(dp[N-1][S])
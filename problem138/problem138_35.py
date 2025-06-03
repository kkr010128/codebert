## coding: UTF-8
mod = 998244353

N, S = map(int,input().split())
A = list(map(int,input().split()))

dp = []
for i in range(N+1):
    #dp.append([0]*3010)
    dp.append([0]*(S+1))
#print(dp)

dp[0][0] = 1
#print(dp)

#print('dpstart')
for i in range(N):
    for j in range(S+1):
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= mod
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= mod        
        if(j >= A[i]):
            dp[i+1][j] += dp[i][j-A[i]]
            dp[i+1][j] %= mod
    #print(dp)

print(dp[N][S])
MOD=10**9+7
N=int(input())
dp=[0]*(N+1)
dp[0]=1

for i in range(N+1):
    for j in range(i-2):
        dp[i]+=dp[j]
        dp[i]%=MOD
print(dp[N])
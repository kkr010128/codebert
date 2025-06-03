N = int(input())
A = list(map(int, input().split()))

dp = [0]*(N)
dp[0] = 1000

for i in range(1,N):
    dp[i] = dp[i-1]
    for j in range(i):
        dp[i] = max(dp[i], (dp[j]//A[j])*A[i]+dp[j]%A[j])
ans = 0
for i in range(N):
    ans = max(ans, dp[i])
print(ans)
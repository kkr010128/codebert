n = int(input())
a = list(map(int, input().split()))

org = [[i, a[i]] for i in range(n)]

lis = sorted(org, key=lambda x: x[1], reverse=True)

dp = [[0 for i in range(n+1)] for j in range(n+1)]


for i in range(0, n, 1):
    for j in range(0, n-i, 1):
        if i + j == n:
            break
            
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + lis[i+j][1]*abs(lis[i+j][0] - i))
        dp[i][j+1] = max(dp[i][j+1], dp[i][j] + lis[i+j][1]*abs(lis[i+j][0] - (n-j-1)))

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])
        
print(ans)
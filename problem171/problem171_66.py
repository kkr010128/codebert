from collections import defaultdict
n = int(input())
a = list(map(int,input().split()))
infants = []
for i in range(n):
    infants.append((a[i],i))
infants.sort()
dp = [defaultdict(int) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    score,initial = infants.pop()
    for right in dp[i].keys():
        dp[i+1][right] = max(dp[i][right]+abs(initial-(i-right))*score,dp[i+1][right])
        dp[i+1][right+1] = max(dp[i][right]+abs((n-1-right)-initial)*score,dp[i+1][right+1])
print(max(dp[n].values()))
n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [0] + [float('inf')]*(n)
for i in range(m):
    for j in range(a[i],n+1):
        dp[j] = min(dp[j],dp[j-a[i]]+1)
        
print(dp[-1])

h,n = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(n)]

dp = [float("inf") for i in range(10**5)]
dp[0] = 0

for a,b in ab:
    for k in range(a+1):
        dp[k] = min(dp[k], b)
    for k in range(a+1,h+1):
        dp[k] = min(dp[k], dp[k-a] + b)
print(dp[h])
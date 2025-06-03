n,m = map(int,input().split(" "))
c = tuple(map(int,input().split(" ")))
m = min(c)
dp = [2**60 for _ in range(n+1)]
dp[0] = 0
for i in range(1,n+1):
    for v in c:
        if i >= v:
            dp[i] = min(dp[i],dp[i-v]+1)
print(dp[n])

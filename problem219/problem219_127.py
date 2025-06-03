N = input().strip()
INFTY = 10**8
dp = [[INFTY for _ in range(2)] for _ in range(len(N)+1)]
a = int(N[-1])
for i in range(10):
    if i<a:
        dp[1][1] = min(dp[1][1],i+10-a)
    else:
        dp[1][0] = min(dp[1][0],i+i-a)
for k in range(2,len(N)+1):
    a = int(N[-k])
    for i in range(10):
        if i>=a:
            dp[k][0] = min(dp[k][0],dp[k-1][0]+i+i-a)
        if i-1>=a:
            dp[k][0] = min(dp[k][0],dp[k-1][1]+i+i-1-a)
        if i<a:
            dp[k][1] = min(dp[k][1],dp[k-1][0]+i+10-a)
        if i==0:
            dp[k][1] = min(dp[k][1],dp[k-1][1]+9-a)
        if 0<=i-1<a:
            dp[k][1] = min(dp[k][1],dp[k-1][1]+i+10-a+i-1)
print(min(dp[len(N)][0],dp[len(N)][1]+1))
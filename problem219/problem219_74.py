S = input().strip()
INFTY=10**8
dp = [[INFTY for _ in range(2)] for _ in range(len(S))]
for k in range(10):
    n = int(S[-1])
    if k>= n:
        dp[0][0] = min(dp[0][0],2*k-n)
    else:
        dp[0][1] = min(dp[0][1],2*k-n+10)
for i in range(1,len(S)):
    n = int(S[-(1+i)])
    for k in range(10):
        if k>n:
            dp[i][0] = min(dp[i][0],2*k-n+dp[i-1][0],k+(k-1)-n+dp[i-1][1])
        elif k==n:
            dp[i][0] = min(dp[i][0],2*k-n+dp[i-1][0])
            if n==0:
                dp[i][1] = min(dp[i][1],k+(k-1)%10-n+dp[i-1][1])
            else:
                dp[i][1] = min(dp[i][1],k+10-n+k-1+dp[i-1][1])
        elif k<n:
            dp[i][1] = min(dp[i][1],k+10-n+k+dp[i-1][0],k+10-n+k-1+dp[i-1][1])
print(min(dp[len(S)-1][0],dp[len(S)-1][1]+1))
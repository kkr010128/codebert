n=int(input())
a=list(map(int,input().split()))
b=[(v,s) for s,v in enumerate(a)]
b.sort(reverse=True)

dp=[[0 for i in range(n+1)] for i in range(n+1)]
for i in range(n+1):
    for j in range(n+1-i):
        if i+j==0:
            continue
        v=b[i+j-1][0]
        pos=b[i+j-1][1]
        if i==0:
            dp[0][j]=dp[0][j-1]+v*abs(n-j-pos)
        elif j==0:
            dp[i][0]=dp[i-1][0]+v*abs(i-1-pos)
        else:
            dp[i][j]=max(dp[i-1][j]+v*abs(i-1-pos),dp[i][j-1]+v*abs(n-j-pos))
ans=0
for i in range(n):
    happy=dp[i][n-i]
    if happy>ans:
        ans=happy
print(ans)
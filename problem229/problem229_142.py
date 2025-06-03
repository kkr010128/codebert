h,n=map(int,input().split())
ab = [list(map(int,input().split())) for i in range(n)]

dp=[float('inf')]*(h+1)
dp[0]=0
for i in range(h):
    for j in range(n):

        next=i+ab[j][0] if i+ab[j][0]<=h else h
        dp[next]=min(dp[next],dp[i]+ab[j][1])
print(dp[-1])

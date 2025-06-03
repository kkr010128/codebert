n,m=map(int,input().split())
c=list(map(int,input().split()))
c.sort()
# print(c) #DB
dp=[[0 for j in range(n+1)] for i in range(m)] # i番目(0<=i<=m-1)までのコインを使用してj円(0<=j<=n)を支払う際の最少の枚数
for j in range(n+1):
    dp[0][j]=j
for i in range(1,m):
    for j in range(n+1):
        if j<c[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=min(dp[i-1][j],dp[i][j-c[i]]+1)
    # print(c[i],dp[i]) #DB
print(dp[m-1][n])

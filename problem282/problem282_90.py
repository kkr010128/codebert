n,t= map(int, input().split())
a= [list(map(int, input().split())) for i in range(n)]


# dp[i][j]: i番目の料理まで見て時間がjの時の満足度のMAX
dpA=[[0]*t for i in range(n+1)]
# dp[i][j]: n-i番目の料理まで見て時間がjのときの満足度のMAX
dpB=[[0]*t for i in range(n+1)]

for i in range(n):
    for j in range(t):
        if a[i][0]>j:
            dpA[i+1][j]=dpA[i][j]
        else:
            dpA[i+1][j]=max(dpA[i][j-a[i][0]]+a[i][1],dpA[i][j])

for i in range(n):
    for j in range(t):
        if a[n-i-1][0]>j:
            dpB[n-i-1][j]=dpB[n-i][j]
        else:
            dpB[n-i-1][j]=max(dpB[n-i][j-a[n-i-1][0]]+a[n-i-1][1],dpB[n-i][j])

ans=0

for i in range(n):
    for j in range(t):
        ans=max(dpA[i][j]+dpB[i+1][t-j-1]+a[i][1],ans)
print(ans)
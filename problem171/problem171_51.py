n=int(input())
a=list(enumerate(map(int,input().split())))
a.sort(key=lambda x: -x[1])
dp=[[0]*(n+1) for i in range(n+1)]
for idx,ix in enumerate(a):
    i,x=ix
    for j in range(idx+1):
        dp[j+1][idx-j]=max(dp[j+1][idx-j],dp[j][idx-j]+(i-j)*x)
        dp[j][idx-j+1]=max(dp[j][idx-j+1],dp[j][idx-j]+((n-1-(idx-j))-i)*x)
print(max([dp[i][n-i] for i in range(n+1)]))
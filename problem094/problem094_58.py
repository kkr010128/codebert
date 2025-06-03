R,C,k = map(int,input().split())
dp1 = [[0]*(C+1) for i in range(R+1)]
dp2 = [[0]*(C+1) for i in range(R+1)]
dp3 = [[0]*(C+1) for i in range(R+1)]
item = [[0]*(C+1) for i in range(R+1)]
for i in range(k):
    r,c,v = map(int,input().split())
    dp1[r][c] = v

for i in range(1,R+1):
    for j in range(1,C+1):
        a = dp1[i][j]
        dp3[i][j] = max(dp2[i][j-1]+a,dp3[i][j-1])
        dp2[i][j] = max(dp1[i][j-1]+a,dp2[i][j-1])
        dp1[i][j] = max(dp1[i-1][j]+a,dp2[i-1][j]+a,dp3[i-1][j]+a,dp1[i][j-1],a)

print(max(dp1[R][C],dp2[R][C],dp3[R][C]))
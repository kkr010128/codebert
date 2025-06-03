R,C,K=map(int,input().split())

V=[[0 for _ in range(C)] for _ in range(R)]

for i in range(K):
    r,c,v=map(int,input().split())
    V[r-1][c-1]=v

dp=[[0 for _ in range(4)] for _ in range(C+1)]
for i in range(R):
    ndp=[[0 for _ in range(4)] for _ in range(C+1)]
    for j in range(C):
        ndp[j][0]=max(dp[j])

    for j in range(C):
        v=V[i][j]
        for n in range(1,4):
            ndp[j][n]=max(ndp[j-1][n-1]+v,dp[j][3]+v,ndp[j-1][n])

    dp=ndp

print(max(dp[C-1]))

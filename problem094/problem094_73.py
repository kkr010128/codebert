from copy import copy

C,R,K=map(int,input().split())
dp=[[0]*(R+1) for i1 in range(4)]
M=[[0]*R for i in range(C)]
for i in range(K):
    r,c,v=map(int,input().split())
    M[r-1][c-1]=v
for i,l in enumerate(M):
    for num in range(1,4):
        for j in range(R):
            if num==1:
                dp[num][j]= max(dp[num][j-1],dp[num-1][j-1]+M[i][j])
            else:
                dp[num][j]= max(dp[num][j-1],dp[num-1][j],dp[num-1][j-1]+M[i][j])
    dp[0]=dp[-1][1:-1]+[0,dp[-1][0]]

print(dp[-1][-2])
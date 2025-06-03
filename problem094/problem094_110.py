import sys
input = sys.stdin.readline
R,C,K = map(int,input().split())
lis = [[0] * (C+1) for i in range(R+1)]
for _ in range(K):
    r,c,v = map(int,input().split())
    lis[r][c] = v

dp = [[[0] * (C+1) for _ in range(R+1)] for _ in range(4)]
#print(dp)
for i in range(1,R+1):
    for j in range(1,C+1):
        for k in range(4):
            dp[0][i][j] = max(dp[0][i][j],dp[k][i-1][j])
            dp[1][i][j] = max(dp[1][i][j],dp[k][i-1][j] + lis[i][j])

            dp[k][i][j] = max(dp[k][i][j],dp[k][i][j-1])
            if k > 0:
                dp[k][i][j] = max(dp[k][i][j],dp[k-1][i][j-1] + lis[i][j])
# print(dp[0])
# print(dp[1])
# print(dp[2])
# print(dp[3])
print(max(dp[0][R][C],dp[1][R][C],dp[2][R][C],dp[3][R][C]))

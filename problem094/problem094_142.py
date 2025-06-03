import sys
input = sys.stdin.buffer.readline
R,C,K = map(int,input().split())
goods = [[0]*(C+1) for _ in range(R+1)]
INF = 10**18
for i in range(K):
    ri,ci,vi = map(int,input().split())
    goods[ri][ci] = vi
DP = [[[-INF]*(C+1) for _ in range(R+1)] for _ in range(4)]
DP[0][1][1] = 0
if goods[1][1]:
    DP[1][1][1] = goods[1][1]
for j in range(1,C):
    DP[0][1][j+1] = 0
    if goods[1][j+1]:
        DP[1][1][j+1] = max(DP[1][1][j],DP[0][1][j]+goods[1][j+1])
        DP[2][1][j+1] = max(DP[2][1][j],DP[1][1][j]+goods[1][j+1])
        DP[3][1][j+1] = max(DP[3][1][j],DP[2][1][j]+goods[1][j+1])
    else:
        DP[1][1][j+1] = DP[1][1][j]
        DP[2][1][j+1] = DP[2][1][j]
        DP[3][1][j+1] = DP[3][1][j]
for i in range(1,R):
    DP[0][i+1][1] = max(DP[0][i][1],DP[1][i][1],DP[2][i][1],DP[3][i][1])
    if goods[i+1][1]:
        DP[1][i+1][1] = DP[0][i+1][1] + goods[i+1][1]
for i in range(2,R+1):
    for j in range(2,C+1):
        DP[0][i][j] = max(DP[0][i-1][j],DP[1][i-1][j],DP[2][i-1][j],DP[3][i-1][j],DP[0][i][j-1])
        if goods[i][j]:
            DP[1][i][j] = max(DP[0][i][j]+goods[i][j],DP[1][i][j-1])
            DP[2][i][j] = max(DP[2][i][j-1],DP[1][i][j-1]+goods[i][j])
            DP[3][i][j] = max(DP[3][i][j-1],DP[2][i][j-1]+goods[i][j])
        else:
            DP[1][i][j] = DP[1][i][j-1]
            DP[2][i][j] = DP[2][i][j-1]
            DP[3][i][j] = DP[3][i][j-1]
print(max(DP[0][R][C],DP[1][R][C],DP[2][R][C],DP[3][R][C]))
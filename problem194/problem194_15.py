H,W = map(int,input().split())
s = [input() for _ in range(H)]

DP = [[1000]+[0]*W for _ in range(H+1)]
re = [[0]*(W+1) for _ in range(H+1)]
DP[0] = [1000]*(W+1)
DP[0][1] = DP[1][0] = 0

for i in range(1,H+1):
    for j in range(1,W+1):
        if s[i-1][j-1] == ".":
            DP[i][j] = min(DP[i-1][j],DP[i][j-1])
        else:
            u = DP[i-1][j]+1-re[i-1][j]
            l = DP[i][j-1]+1-re[i][j-1]
            DP[i][j] = min(u, l)
            re[i][j] = 1

print(DP[H][W])

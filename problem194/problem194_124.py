H,W = map(int,input().split())
map = []
INF = 10**8
for _ in range(H):
    map.append(input())

dp = [[0 for i in range(W)] for i in range(H)]

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            if map[i][j] == '#':
                dp[i][j] = 1
        elif i == 0:
            flag = 0
            if map[i][j] == '#' and map[i][j-1] == '.':
                flag = 1
            dp[i][j] = flag + dp[i][j-1]
        elif j == 0:
            flag = 0
            if map[i][j] == "#" and map[i-1][j] == ".":
                flag = 1
            dp[i][j] = flag + dp[i-1][j]
        else:
            flag1 = 0
            flag2 = 0
            if map[i][j] == "#" and map[i][j-1] == ".":
                flag1 = 1
            if map[i][j] == "#" and map[i-1][j] == ".":
                flag2 = 1
            dp[i][j] = min(dp[i][j-1]+flag1,dp[i-1][j]+flag2)

print(dp[H-1][W-1])

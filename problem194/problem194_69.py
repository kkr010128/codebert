H, W = map(int, input().split())
Maze = [[1 if a == "#" else 0 for a in input()] for _ in range(H)]

DP = [[float('inf')] * W for _ in range(H)]

if Maze[0][0] == 1:
    DP[0][0] = 1
else:
    DP[0][0] = 0

for i in range(H):
    for j in range(W):
        if Maze[i][j] == 1:
            if i + 1 < H:
                DP[i+1][j] = DP[i][j]
            if j + 1 < W:
                DP[i][j+1] = min(DP[i][j+1], DP[i][j])
        if Maze[i][j] == 0:
            if i + 1 < H:
                if Maze[i+1][j] != 1:
                    DP[i + 1][j] = DP[i][j]
                else:
                    DP[i + 1][j] = DP[i][j] + 1
            if j + 1 < W:
                if Maze[i][j + 1] != 1:
                    DP[i][j + 1] = min(DP[i][j + 1], DP[i][j])
                else:
                    DP[i][j + 1] = min(DP[i][j + 1], DP[i][j]+1)

print(DP[H-1][W-1])

H, W = map(int, input().split(' '))
s = []
for _ in range(H):
    s.append(input())

dp = [[10 ** 9 for i in range(W)] for j in range(H)]
dp[0][0] = 0 if s[0][0] == '.' else 1

for i in range(H):
    for j in range(W):
        if i + 1 < H:
            cost = int(s[i][j] == '.' and s[i + 1][j] == '#')
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + cost)
        if j + 1 < W:
            cost = int(s[i][j] == '.' and s[i][j + 1] == '#')
            dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + cost)

print(dp[H - 1][W - 1])
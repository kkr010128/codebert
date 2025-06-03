h, w = map(int, input().split())
g = [[0] * w for _ in range(h)]#白が1、黒が０
for i in range(h):
    s = list(input())
    for j in range(w):
        if s[j] == '.':
            g[i][j] = 1
INF = 10**9
dp = [[INF] * w for _ in range(h)]
if g[0][0] == 0:
    dp[0][0] = 1
else:
    dp[0][0] = 0

for i in range(h):
    for j in range(w):
        for dx, dy in ((1, 0), (0, 1)):
            nx = j + dx
            ny = i + dy
            if ny >= h or nx >= w:
                continue
            add = 0
            if g[ny][nx] == 0 and g[i][j]  == 1:
                add = 1
            dp[ny][nx] = min(dp[ny][nx], dp[i][j] + add)
            
print(dp[h-1][w-1])



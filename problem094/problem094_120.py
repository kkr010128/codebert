R, C, K = map(int, input().split())
item = [[0]*C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    item[r-1][c-1] = v
dp = [[[0]*C for _ in range(R)] for _ in range(4)]
dp[1][0][0] = item[0][0]

for h in range(R):
    for w in range(C):
        if h!=0:
            dp[0][h][w] = max(dp[0][h][w], dp[0][h-1][w], dp[1][h-1][w],  dp[2][h-1][w],  dp[3][h-1][w])
            dp[1][h][w] = max(dp[1][h][w], dp[0][h-1][w]+item[h][w], dp[1][h-1][w]+item[h][w], dp[2][h-1][w]+item[h][w], dp[3][h-1][w]+item[h][w])
        if w!=0:
            dp[0][h][w] = max(dp[0][h][w], dp[0][h][w-1])
            dp[1][h][w] = max(dp[1][h][w], dp[1][h][w-1], dp[0][h][w-1]+item[h][w])
            dp[2][h][w] = max(dp[2][h][w], dp[2][h][w-1], dp[1][h][w-1]+item[h][w])
            dp[3][h][w] = max(dp[3][h][w], dp[3][h][w-1], dp[2][h][w-1]+item[h][w])
ans = []
for k in range(4):
    ans.append(dp[k][-1][-1])
print(max(ans))
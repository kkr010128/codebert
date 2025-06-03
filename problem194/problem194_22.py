# AGC 043 A
H,W = map(int, input().split())
table = [input() for _ in range(H)]

inf = 10**9
dp = [[inf] * (W+1) for _ in range(H+1)]
dp[0][0] = 0 if table[0][0] == "." else 1

for h in range(H):
    for w in range(W):
        flg = table[h][w] == "." and (table[h][w+1] == "#" if w < W-1 else True) 
        dp[h][w+1] = min(dp[h][w+1], dp[h][w] + 1 if flg else dp[h][w])

        flg = table[h][w] == "." and (table[h+1][w] == "#" if h < H-1 else True)
        dp[h+1][w] = dp[h][w] + 1 if flg else dp[h][w]

print(dp[H-1][W-1])

H, W = map(int, input().split())
dp = [[H*W for __ in range(W)] for _ in range(H)]
dh = [1, 0]
dw = [0, 1]
S = []
for i in range(H):
    s = input()
    S.append(s)

if (S[0][0] == '#'):
    dp[0][0] = 1
else:
    dp[0][0] = 0


for i in range(H):
    for j in range(W):
        for k in range(2):
            nh = i + dh[k]
            nw = j + dw[k]
            if nh >= H or nw >= W:
                continue
            add = 0
            if (S[nh][nw] == "#" and S[i][j] == "."):
                add = 1
            dp[nh][nw] = min(dp[nh][nw], dp[i][j] + add)


print(dp[H-1][W-1])

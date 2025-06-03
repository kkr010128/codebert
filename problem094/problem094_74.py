H,W,k = map(int, input().split())
# アイテムが何処に何個あるか
fs = [[0]*(W+1) for i in range(H+1)]
for i in range(k):
    h, w, v = map(int, input().split())
    h -= 1
    w -= 1
    fs[h][w] = v

mvs = [(0,1),(1,0)]
dp = [[[-1<<50 for i in range(W+1)] for j in range(H+1)] for k in range(4)]
# dp[n][i][j] n個取ったときの、i,jにおけるアイテム価値の最大値
from collections import deque
q = deque([])
q.append((0,0))
dp[0][0][0] = 0
dp[1][0][0] = fs[0][0]
for h in range(H):
    for w in range(W):
        dp[0][h][w+1] = max(dp[0][h][w+1], dp[0][h][w])
        dp[1][h][w+1] = max(dp[1][h][w+1], dp[1][h][w], dp[0][h][w] + fs[h][w+1])
        dp[2][h][w+1] = max(dp[2][h][w+1], dp[2][h][w], dp[1][h][w] + fs[h][w+1])
        dp[3][h][w+1] = max(dp[3][h][w+1], dp[3][h][w], dp[2][h][w] + fs[h][w+1])
    for w in range(W):
        mx = 0
        for i in range(4):
            # print("fe",i,h,w,"dp",dp[i][h][w])
            mx = max(mx,dp[i][h][w])
        dp[0][h+1][w] = mx
        dp[1][h+1][w] = mx + fs[h+1][w]

H -= 1
W -= 1
ans0 = dp[0][H][W]
ans1 = dp[1][H][W]
ans2 = dp[2][H][W]
ans3 = dp[3][H][W]
# print(fs)
# for i in range(3):
#     d = dp[i]
#     for r in d:
#         print(*r)
#     print("----------")
print(max(ans1,ans2,ans3))
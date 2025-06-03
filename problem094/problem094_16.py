R,C,K = map(int,input().split())

item = [[0] * (C + 1) for _ in range(R + 1)]
for i in range(K):
    r,c,v = map(int,input().split())
    item[r][c] = v

dp = [[[0]*(C+1) for _ in range(R+1)] for _ in range(4)]

for h in range(R+1):
    for w in range(C+1):
        for k in range(4):
            position = dp[k][h][w]
            if h+1 <= R:
                # 移動先のアイテムを取らない場合
                dp[0][h+1][w] = max(dp[0][h+1][w], position)
                 # 移動先のアイテムを取る場合
                dp[1][h+1][w] = max(dp[1][h+1][w], position+item[h+1][w])
            if w+1 <= C:
                # 移動先のアイテムを取らない場合
                dp[k][h][w+1] = max(dp[k][h][w+1], position)
                # 現在のkが3未満のときのみ, 移動先のアイテムを取ることが可能
                if k < 3:
                    dp[k+1][h][w+1] = max(dp[k+1][h][w+1], position+item[h][w+1])

ans = 0
for k in range(4):
    ans = max(ans, dp[k][-1][-1])

print(ans)
N, T = map(int, input().split())

dishes = sorted([tuple(map(int,input().split())) for i in range(N)])

dp = [[0] * 3100 for _ in range(3100)]
ans = 0

for i in range(1, N + 1):
    for j in range(1, T):
#dpをもとにした最大値の更新
        dp[i][j] = dp[i-1][j] 
        ans = max(ans, dp[i][j] + dishes[i-1][1]) #最後に、最も時間のかかるものを食べて、大きい場合は最大値（ans）を更新

# dpの更新
        if j - dishes[i-1][0] >= 0: #最後に食べる品が持ち時間より長いばあいはNG
            dp[i][j] = max(dp[i][j], dp[i-1][j-dishes[i-1][0]] + dishes[i-1][1]) #ラストオーダーまでにj-dishes[i-1][0]の時間があるので

print(ans)
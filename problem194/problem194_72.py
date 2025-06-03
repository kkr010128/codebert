H, W = map(int, input().split())
grid = [input() for _ in range(H)]

inf = 10**18
# dp[i][j]はi.j点に行くまでに何回白→黒の変化があったか
dp = [[inf] * W for _ in range(H)]
if grid[0][0] == "#":
    dp[0][0] = 1
else:
    dp[0][0] = 0

for i in range(H):
    for j in range(W):
        if i != 0: # 下移動
            # 今いてるのがi,j点、前の点(上)が白で次が黒なら1足す
            tmp = dp[i - 1][j] + int(grid[i][j]=="#" and grid[i - 1][j]==".")
            dp[i][j] = min(dp[i][j], tmp)
        if j != 0: # 右移動
            # 前の点(左)が白で次が黒なら1足す
            tmp = dp[i][j - 1] + int(grid[i][j]=="#" and grid[i][j - 1]==".")
            dp[i][j] = min(dp[i][j], tmp)
        # この一連の処理で、i,j点に、下移動した場合と右移動した場合のうちの最小値が得られる。
# こたえは目的地, i.e. 右下の点のdpの値
ans = dp[H - 1][W - 1]
print(ans)
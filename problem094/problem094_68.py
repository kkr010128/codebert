r, c, k = map(int, input().split())
rcv = [list(map(int, input().split())) for i in range(k)]

area = [[0] * (c+1) for i in range(r+1)]
for a, b, v in rcv:
    area[a-1][b-1] = v

# dp[i][j][k]: その行でiまで拾っており、
# j行k列目に到達時点の最大スコア
dp = [[[-1] * (c+1) for i in range(r+1)] for j in range(4)]
dp[0][0][0] = 0

for rr in range(r+1):
    for cc in range(c+1):
        for i in range(4):
            # 取って右
            if i+1<4 and cc<c and area[rr][cc]>0:
                dp[i+1][rr][cc+1] = max(dp[i+1][rr][cc+1],
                                        dp[i][rr][cc]+area[rr][cc])
            # 取って下
            if i+1<4 and rr<r and area[rr][cc]>0:
                dp[0][rr+1][cc] = max(dp[0][rr+1][cc],
                                      dp[i][rr][cc]+area[rr][cc])
            # 取らずに右
            if cc<c:
                dp[i][rr][cc+1] = max(dp[i][rr][cc+1],
                                      dp[i][rr][cc])
            # 取らずに下
            if rr<r:
                dp[0][rr+1][cc] = max(dp[0][rr+1][cc],
                                      dp[i][rr][cc])
# ans: r行c列目の最大値（iは問わず）
ans = max([dp[i][r][c] for i in range(4)])
print(ans)




R, C, K = map(int, input().split())

V = [[0]*(C+1) for _ in range(R+1)]
for _ in range(K):
    r, c, v = map(int, input().split())
    V[r][c] = v

max_pre = [0]*(C+1)
for i in range(R+1):
    now = [[0]*(3+1) for _ in range(C+1)]
    for j in range(C+1):
        v = V[i][j]
        la = lb = 0
        if j > 0:
            la = now[j-1][0]
            lb = now[j-1][1]
            now[j][2] = max(now[j][2], now[j-1][2], lb + v)
            now[j][3] = max(now[j][3], now[j-1][3], now[j-1][2] + v)
        if i > 0:
            now[j][0] = max(now[j][0], max_pre[j], la)
            now[j][1] = max(now[j][1], max_pre[j] + v, la + v, lb)
        max_pre[j] = max(now[j])

print(max(now[C]))

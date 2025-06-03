import sys

input = sys.stdin.readline

R, C, K = map(int, input().split())
D = dict()
for _ in range(K):
    r, c, v = map(int, input().split())
    D[(r, c)] = v

dp0 = [[0] * (C + 1) for _ in range(R + 1)]
dp1 = [[0] * (C + 1) for _ in range(R + 1)]
dp2 = [[0] * (C + 1) for _ in range(R + 1)]
dp3 = [[0] * (C + 1) for _ in range(R + 1)]

for r in range(1, R + 1):
    for c in range(1, C + 1):
        m = max(dp0[r - 1][c], dp1[r - 1][c], dp2[r - 1][c], dp3[r - 1][c])
        dp0[r][c] = max(m, dp0[r][c - 1])
        dp1[r][c] = max(m, dp1[r][c - 1])
        dp2[r][c] = max(m, dp2[r][c - 1])
        dp3[r][c] = max(m, dp3[r][c - 1])
        if (r, c) in D:
            dp1[r][c] = max(dp1[r][c], m + D[(r, c)], dp0[r][c - 1] + D[(r, c)])
            dp2[r][c] = max(dp2[r][c], m + D[(r, c)], dp1[r][c - 1] + D[(r, c)])
            dp3[r][c] = max(dp3[r][c], m + D[(r, c)], dp2[r][c - 1] + D[(r, c)])
print(max(dp0[-1][-1], dp1[-1][-1], dp2[-1][-1], dp3[-1][-1]))

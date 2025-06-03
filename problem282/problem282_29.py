#145_E
n, t = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

#dp1[i][j] ... 1~iでj分以内の最大値
#dp2[i][j] ... i~nでj分以内の最大値
dp1 = [[0 for _ in range(t)] for _ in range(n+1)]
dp2 = [[0 for _ in range(t)] for _ in range(n+2)]

for i in range(1, n+1):
    a, b = ab[i-1]
    for j in range(1, t):
        if j - a >= 0:
            dp1[i][j] = max(dp1[i-1][j], dp1[i-1][j-a] + b)
        else:
            dp1[i][j] = dp1[i-1][j]

for i in range(n, 0, -1):
    a, b = ab[i-1]
    for j in range(1, t):
        if j - a >= 0:
            dp2[i][j] = max(dp2[i+1][j], dp2[i+1][j-a] + b)
        else:
            dp2[i][j] = dp2[i+1][j]

ans = 0
for i in range(1, n+1):
    b = ab[i-1][1]
    for j in range(0, t):
        x = dp1[i-1][j] + dp2[i+1][t-j-1] + b
        ans = max(ans, x)

print(ans)
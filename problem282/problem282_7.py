n, t = map(int, input().split())
a, b, ab = [], [], []
for _ in range(n):
    ab.append(tuple(map(int, input().split())))
ab.sort(key=lambda x:x[0])
for i in ab:
    a.append(i[0])
    b.append(i[1])

# dp[i][j] = 0~i番目の料理でj分以内に完食できる美味しさの合計の最大値
# 0 <= i < n-1, 0 <= j <= t-1
dp = [[0 for _ in range(min([t, a[0]]))] + [b[0] for _ in range(t-a[0])]]
for i in range(1, n-1):
    dp.append([])
    for j in range(min([t, a[i]])):
        dp[i].append(dp[i-1][j])
    for j in range(a[i], t):
        dp[i].append(max([dp[i-1][j], dp[i-1][j-a[i]]+b[i]]))

ans = []
for i in range(1, n):
    ans.append(dp[i-1][t-1] + b[i])
print(max(ans))
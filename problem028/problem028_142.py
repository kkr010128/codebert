n,m = map(int,input().split())
c = list(map(int,input().split()))
i = 0
dp = [0] * 50001
for i in range(50001):
    dp[i] = i
#金額ごとに最小枚数を出す
for i in range(2,n+1):
    for j in range(m):
        if i - c[j] >= 0:
            dp[i] = min(dp[i], dp[i - c[j]] + 1)

print(dp[n])

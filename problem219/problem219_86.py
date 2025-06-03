s = input()
s = '0' + s[::-1]
dp = [[0, 0] for _ in range(len(s) + 1)]
for i in range(len(s)):
    for j in range(2):
        if j == 0: #ぴったり
            dp[i + 1][j] = min(dp[i]) + int(s[i])
        else: #1枚多めに払う
            dp[i + 1][j] = min(dp[i][1] + 9 - int(s[i]), dp[i][0] + 11 - int(s[i]))

print(min(dp[-1]))
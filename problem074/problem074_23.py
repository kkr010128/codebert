n, k = [int(_) for _ in input().split()]
s = []
for i in range(k):
    s.append([int(_) for _ in input().split()])
dp = [0 for i in range(n)]
dp[0] = 1
dp_s = [0 for i in range(n+1)]
dp_s[1] = 1
for i in range(1, n):
    for j in range(len(s)):
        r, l = s[j]
        if i-r >= 0:
            if i-l >= 0:
                dp[i] += dp_s[i-r+1] - dp_s[i-l]
            else:
                dp[i] += dp_s[i-r+1] - dp_s[0]
    dp[i] = dp[i] % 998244353
    dp_s[i+1] += dp_s[i] + dp[i]
    dp_s[i+1] = dp_s[i+1] % 998244353
print(dp[-1])
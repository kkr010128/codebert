dp = [False] * 100200
dp[0] = True
for x in range(100000):
    if dp[x]:
        for i in range(100, 106):
            dp[x+i] = True
print(int(dp[int(input())]))
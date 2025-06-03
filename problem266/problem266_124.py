x = int(input())
dp = [False] * (x + 1)
dp[0] = True

items = [100, 101, 102, 103, 104, 105]
for i in items:
    for j in range(x + 1):
        if j + i >= x + 1:
            break
        dp[j + i] |= dp[j]
if dp[x]:
    print(1)
else:
    print(0)
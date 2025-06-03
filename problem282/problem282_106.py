n, W = map(int, input().split())
ab = [tuple(map(int, input().split()))for _ in range(n)]
ab.sort()

ans = 0
dp = [0]*W
for a, b in ab:
    if ans < dp[-1]+b:
        ans = dp[-1]+b
    for j in reversed(range(W)):
        if j-a < 0:
            break
        if dp[j] < dp[j-a]+b:
            dp[j] = dp[j-a]+b
print(ans)

n, m = map(int, input().split())
C = sorted([int(x) for x in input().split()])
dp = [int(x) for x in range(n + 1)]
for c in C[1:]:
    for i in range(n + 1):
        anc = i - c
        if anc < 0:
            continue
        dp[i] = min(dp[i], dp[anc] + 1)
print(dp[n])


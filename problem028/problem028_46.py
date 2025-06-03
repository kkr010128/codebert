import sys
input = sys.stdin.readline


def inpl():
    return list(map(int, input().split()))


N, M = inpl()
coins = inpl()

dp = [i for i in range(N + 1)]
coins.sort()

for n in range(coins[1], N + 1):
    for c in coins[1:]:
        if c > n:
            continue
        dp[n] = min(dp[n], dp[n - c] + 1)

# print(dp[N])
print(dp[N])


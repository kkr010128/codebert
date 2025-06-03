n, m = map(int, input().split())
coins = list(map(int, input().split()))
memo = [0] + [10**7] * n
for coin in coins:
    for i in range(coin, n+1):
        memo[i] = min(memo[i], memo[i-coin]+1)
print(memo[-1])


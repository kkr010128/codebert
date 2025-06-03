n, k = map(int, input().split())
# n, k = (2*10**5, 10)


ranges = []
for i in range(k):
    l, r = map(int, input().split())
    # f = (2 * 10 ** 5) // k
    # l, r = (f * i, f*(i+1))
    ranges.append((l, r))

mod = 998244353
counts = [0]*(n+1)
sum_dp = [0]*(n+2)
counts[0] = 1
sum_dp[1] = 1
for i in range(1, n+1):
    for r in ranges:
        left = max(0, i - r[1])
        right = max(0, i - r[0] + 1)
        counts[i] += (sum_dp[right] - sum_dp[left])
        counts[i] = counts[i] % mod
    sum_dp[i+1] = sum_dp[i] + counts[i]


print(counts[n-1] % mod)
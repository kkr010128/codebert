import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

mod = 998244353

n, k = map(int, input().split())
l = []
r = []
for _ in range(k):
    l_, r_ = map(int, input().split())
    l.append(l_)
    r.append(r_)
dp = [0] * (n + 1)
dp_csum = [0] * (n + 1)
dp[1] = 1
dp_csum[1] = 1
for i in range(2, n + 1):
    for j in range(k):
        left = i - r[j]
        right = i - l[j]
        if right >= 1:
            dp[i] += dp_csum[right] - dp_csum[max(left, 1) - 1]
            dp[i] %= mod
    dp_csum[i] = dp_csum[i - 1] + dp[i]
    dp_csum[i] %= mod
print(dp[-1])
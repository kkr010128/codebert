n, k = map(int, input().split())
lr = []
for _ in range(k):
    lr.append(tuple(map(int, input().split())))
mod = 998244353

dp = [0]*n
dp[0] = 1

acc = [0]*n
acc[0] = 1

for i in range(1, n):
    for l, r in lr:
        if 0 <= i-r and i-l < i:
            dp[i] += acc[i-l]-acc[i-r-1]
        elif i-r < 0 and i-l < i:
            dp[i] += acc[i-l]
        elif i-r < 0 and i <= i-l:
            dp[i] += acc[i-1]
        elif 0 < i-r and i <= i-l:
            dp[i] += acc[i-1]-acc[i-r-1]
    acc[i] = acc[i-1]+dp[i]%mod

print(dp[-1]%mod)
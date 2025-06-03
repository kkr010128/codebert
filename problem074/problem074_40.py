n, k = map(int, input().split())

mod = 998244353

m_list = []

for _ in range(k):
    m_list.append(list(map(int, input().split())))

dp = [0]*n
dp[0] = 1

dp_sum = [0]*n
dp_sum[0] = 1

for i in range(1, n):
    for j in range(k):
        l, r = m_list[j]
        il = i-l
        ir = i-r-1
        if il < 0:
            continue
        else:
            if ir < 0 :
                dp[i] += dp_sum[il]
            else:
                dp[i] += dp_sum[il] - dp_sum[ir]
            dp[i] %= mod
    dp_sum[i] = dp_sum[i-1] + dp[i]
    dp_sum[i] %= mod

print(dp[n-1] % mod)
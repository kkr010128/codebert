MODINT = 10**9+7
n, k = map(int, input().split())

ans = 0

"""
dp[i] =　gdc がi となる場合のgcdの総和
"""
dp = [0] * (k+100)
for i in range(k, 0, -1):
    dp[i] = pow(k//i, n, MODINT)
    for j in range(i*2, k+1, i):
        dp[i] -= dp[j]
    ans += (dp[i]*i)%MODINT
print(ans%MODINT)
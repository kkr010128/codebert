N, S = map(int, input().split())
A_array = list(map(int, input().split()))

mod = 998244353

a = 1
arr2 = [1]
ans = 0
for i in range(N):
    a = a * 2 % mod
    arr2.append(a)

dp = [0] * (S + 1)
dp[0] = 1

for i, a in enumerate(A_array):
    # print(dp)
    if S - a >= 0:
        ans = (ans + dp[S - a] * arr2[N - 1 - i]) % mod
    for j in range(S, -1, -1):
        dp[j] = (2 * dp[j] + (dp[j - a] if (j - a) >= 0 else 0)) % mod
print(ans)

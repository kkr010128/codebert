MOD = 998244353

n, k = map(int, input().split())
l = [0] * k
r = [0] * k
for i in range(k):
    l[i], r[i] = map(int, input().split())

s = [0] * (n + 2)
for i in range(k):
    for j in range(l[i], r[i] + 1):
        s[j] = 1

ans = [0] * (n + 1)
ans[0] = 1
for i in range(n - 1):
    ans[i + 1] = ans[i]
    for j in range(k):
        ans[i + 1] += ans[max(-1, i + 1 - l[j])]
        ans[i + 1] -= ans[max(-1, i + 1 - r[j] - 1)]
        ans[i + 1] = ans[i + 1] % MOD
print((ans[n - 1] - ans[n - 2]) % MOD)

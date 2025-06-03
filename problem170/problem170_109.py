MOD = 10 ** 9 + 7
n, k = map(int, input().split())
ans = 0
for x in range(k, n + 2):
    p = x * (x - 1) // 2
    q = x * (x - 1) // 2 + (n - x + 1) * x
    ans += q - p + 1
print(ans % MOD)

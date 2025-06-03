n, m, k = map(int, input().split())
MOD = 998244353
ans = 0
c = 1

for i in range(k + 1):
    ans += (((m * pow(m - 1, n - i - 1, MOD)) % MOD) * c) % MOD
    ans %= MOD
    c = (c * (n - 1 - i) * pow(i + 1, MOD - 2, MOD)) % MOD
    
    
print(ans%MOD)
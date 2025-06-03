MAX = 600000
MOD = 998244353
fac = [0] * MAX
ifac = [0] * MAX
fac[0] = 1
for i in range(1,MAX):
    fac[i] = (fac[i-1] * i) % MOD
ifac[MAX-1] = pow(fac[MAX-1],MOD-2,MOD)
for i in reversed(range(1,MAX)):
    ifac[i-1] = (ifac[i] * i) % MOD

def combinations(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return (fac[n] * ifac[k] * ifac[n-k]) % MOD
n, m, k = map(int ,input().split())
ans = 0
color = m
for i in reversed(range(n)):
    val = color
    val *= combinations(n-1,i)
    val %= MOD
    if i <= k:
        ans += val
        ans %= MOD
    color *= (m-1)
    color %= MOD
print(ans)

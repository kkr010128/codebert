n, m, k = list(map(int, input().split()))
mod = 998244353
m_ = m - 1
n_ = n - 1
m_p = {0: 1}
ans = 0
fac = {0: 1, 1: 1}
finv = {0: 1, 1: 1}
inv = {1: 1}

def comb_init():
    for i in range(2, n + 1):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
def comb(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod
def pow_init(m):
    for i in range(1, m):
        m_p[i] = m_p[i - 1] * m_
        m_p[i] %= mod

comb_init()
pow_init(n_ - k)
for i in range(k, -1, -1):
    if n_ - i not in m_p:
        m_p[n_ - i] = m_p[n_ - i - 1] * m_ % mod
    d = m * comb(n_, i) % mod 
    d *= m_p[n_ - i]
    ans += d % mod
    ans %= mod
print(ans)
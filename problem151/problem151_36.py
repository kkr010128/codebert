n,m,k = map(int, input().split())

# ---------------------------------------
# nCr(n, r, m) テンプレ
mod = 998244353

fac = [1,1] # 階乗 n!
inv = [0,1] # 逆元 1/n
finv = [1,1] # 逆元の階乗 (n^-1)! = (1/n)!

for i in range(2, n+1):
    fac.append( (fac[-1] * i ) % mod )
    inv.append( (-inv[mod%i] * (mod//i)) % mod )
    finv.append( (finv[-1] * inv[-1]) % mod )

def nCr(n, r, m):
    if (n<0 or r<0 or n<r): return 0
    r = min(r, n-r)
    return fac[n] * finv[n-r] * finv[r] % m
# ----------------------------

ans = 0
colors = m
for p in range(n-1, -1, -1):
    if p <= k:
        groups = nCr(n-1, p, mod)
        ans += groups * colors % mod
        ans %= mod
    colors *= m - 1
    colors %= mod
ans += mod
ans %= mod
print(ans)

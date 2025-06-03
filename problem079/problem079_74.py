# nCr(n, r, m): 組合せ
# nHr(n, r, m): 重複組合せ
MOD = 10**9 + 7
fac = [1,1] # 階乗 n!
inv = [0,1] # 逆元 1/n
finv = [1,1] # 逆元の階乗 (n^-1)! = (1/n)!

def finv_init(n, m):
    for i in range(2, n+1):
        fac.append( (fac[-1] * i ) % m )
        inv.append( (-inv[m%i] * (m//i)) % m )
        finv.append( (finv[-1] * inv[-1]) % m )

def nCr(n, r, m):
    if (n<0 or r<0 or n<r): return 0
    r = min(r, n-r)
    return fac[n] * finv[n-r] * finv[r] % m

def nHr(n, r, m): return nCr(n+r-1, r, m)

s = int(input())
finv_init(s, MOD) # 初期設定
ans = 0
for n in range(1, s+1):
    if s < 3*n: break
    ans += nHr(n, s - 3*n, MOD)
print(ans % MOD)

k=int(input())
s=list(input())

n=len(s)

def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod

def p(n,r,mod):
    return fact[n]*factinv[n-r] % mod
mod = 10 ** 9 + 7
maxi = 2*10 ** 6 + 1  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, maxi + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

array_5=[1]
array_6=[1]
for i in range(k):
    array_5.append(25*array_5[-1]%mod)
    array_6.append(26*array_6[-1]%mod)

ans=0
for i in range(n,n+k+1): #iはS_Nの固定した位置を表す。
    x=cmb(i-1,n-1,mod)
    y=array_5[i-n]*array_6[n+k-i]
    ans += x*y%mod
    ans %=mod
print(ans)
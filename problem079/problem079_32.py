def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return (fact[n] * factinv[r] * factinv[n-r]) % mod

def prm(n,r,mod):
    if (r < 0) or (n < r):
        return 0
    return (fact[n] * factinv[n-r])%mod
mod = 10**9 + 7

fact = [1, 1]
factinv = [1, 1]
inv = [0,1]

s = int(input())
na = s//3
ans = 0

for i in range(2,s):
    fact.append((fact[-1] * i) % mod)
    inv.append((inv[mod % i] * (mod - (mod // i))) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

for i in range(1,na+1):
    ans += cmb(s - 3*i + i - 1, i-1 , mod)
    ans %= mod
print(ans%mod)
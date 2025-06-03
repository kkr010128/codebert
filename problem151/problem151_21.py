n,m,k = map(int,input().split())
mod = 998244353
ans = 0
fact = [1,1]
finv = [1,1]
for i in range(2, n+1):
    fact += [fact[i-1] * i % mod]
    finv += [pow(fact[i], mod-2, mod)]


def comb(n,k, mod):
    return (fact[n] * finv[k] * finv[n-k]) % mod



for i in range(0, k+1):
    ans += m * pow(m-1, n-i-1, mod) * comb(n-1, i, mod)
    ans %= mod
print(ans)
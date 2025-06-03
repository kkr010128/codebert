n,k = map(int,input().split())
mod = 10**9 + 7

fact = [1]
finv = [1]
for i in range(1, 2*n):
    fact.append((fact[i-1] * i) % mod)
    finv.append(pow(fact[i], mod-2, mod))

if n-1 <= k:
    print((fact[2*n-1] * finv[n] * finv[n-1]) % mod)
    exit()

ans = 0
for i in range(k+1):
    ans += fact[n] * finv[n-i] * finv[i] * fact[n-1] * finv[n-1-i] * finv[i]
    ans %= mod

print(ans)
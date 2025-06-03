p = 998244353
max = 2 * (10**5)
fact = [1,1]
facti = [1,1]
inv = [0,1]
for i in range(2, max + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    facti.append((facti[-1] * inv[-1]) % p)

def comb(n,r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * facti[r] * facti[n-r] % p

n,m,k = map(int, input().split())
ans = 0
for i in range(k+1):
    a = comb(n-1,i)
    b = m * pow(m-1,n-1-i,998244353)
    ans += (a * b)% 998244353
print(ans%998244353)
def setFact(n, mod):
    global fact
    global ifact
    fact = [0]*(n+1)
    fact[0] = 1
    ifact = [0] * (n+1)
    for i in range(1, n+1):
        fact[i] = (fact[i-1]*i)%mod
    ifact[n] = pow(fact[n], mod-2, mod)
    for i in range(1, n+1):
        ifact[n-i] = ifact[n-i+1]*(n-i+1)%mod
def combination(n, k, mod):
    global fact
    global ifact
    if k < 0 or k > n:
        return 0
    else:
        return fact[n]*ifact[n-k]*ifact[k]%mod
k = int(input())
s = input()
n = len(s)
mod = 10**9 + 7
ans = 0
setFact(n+k, mod)
for i in range(k+1):
    now = 1
    now *= pow(26, i, mod)
    now %= mod
    now *= pow(25, k-i, mod)
    now %= mod
    now *= combination(k-i+n-1,n-1 , mod)
    now %= mod
    ans += now
    ans %= mod
print(ans)
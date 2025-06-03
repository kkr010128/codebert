MOD = 10**9+7
k = int(input())
s = input()
n = len(s)
 
 
U = n+k
fact = [0]*(U+1)
fact[0] = 1
for i in range(1, U+1):
    fact[i] = fact[i-1]*i % MOD
 
 
invfact = [0]*(U+1)
invfact[U] = pow(fact[U], MOD-2, MOD)
for i in reversed(range(U)):
    invfact[i] = invfact[i+1]*(i+1) % MOD
 
 
def nCr(n, r):
    if r < 0 or n < r:
        return 0
    return fact[n]*invfact[r]*invfact[n-r]
 
 
ans = 0
for x in range(k+1):
    ans += pow(26, x, MOD)*nCr(n+k-x-1, n-1)*pow(25, k-x, MOD)
    ans %= MOD
print(ans)
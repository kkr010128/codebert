U = 2*10**6+1
MOD = 10**9+7
 
fact = [1]*(U+1)
fact_inv = [1]*(U+1)
 
for i in range(1,U+1):
    fact[i] = (fact[i-1]*i)%MOD
fact_inv[U] = pow(fact[U], MOD-2, MOD)
 
for i in range(U,0,-1):
    fact_inv[i-1] = (fact_inv[i]*i)%MOD

def comb(n, k):
    if k < 0 or k > n:
        return 0
    z = fact[n]
    z *= fact_inv[k]
    z *= fact_inv[n-k]
    z %= MOD
    return z

k = int(input())
S = input()
n = len(S)
ans = 0
for i in range(n-1, n+k):
  temp = comb(i, n-1)*pow(25, i-(n-1), MOD)*pow(26, n+k-1-i, MOD)
  temp %= MOD
  ans += temp
ans %= MOD
print(ans)
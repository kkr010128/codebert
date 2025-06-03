import sys
input = sys.stdin.buffer.readline

mod = 10**9+7
MAX_N = 10**7 + 10

fact = [1]
fact_inv = [0]*(MAX_N+4)
for i in range(MAX_N+3):
    fact.append(fact[-1]*(i+1)%mod)

fact_inv[-1] = pow(fact[-1],mod-2,mod)
for i in range(MAX_N+2,-1,-1):
    fact_inv[i] = fact_inv[i+1]*(i+1)%mod


def mod_comb_k(n,k,mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n-k] %mod

k = int(input())
s = list(input())

n = len(s)-1

res = 0

for i in range(n,n+k+1):
    res = (res + (mod_comb_k(i-1,n-1,mod)*pow(25,i-n,mod)%mod)*pow(26,n+k-i,mod))%mod

print(res)
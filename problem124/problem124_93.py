k = int(input())
s = input()
L = len(s)
mod = 10**9+7

MAX = 2*10**6
fact = [1]*(MAX+1)
for i in range(1, MAX+1):
    fact[i] = (fact[i-1]*i) % mod

inv = [1]*(MAX+1)
for i in range(2, MAX+1):
    inv[i] = inv[mod % i]*(mod-mod//i) % mod

fact_inv = [1]*(MAX+1)
for i in range(1, MAX+1):
    fact_inv[i] = fact_inv[i-1] * inv[i] % mod

def comb(n, k):
    if n < k:
        return 0
    return fact[n] * fact_inv[n-k] * fact_inv[k] % mod
  
p25 = [1]*(k+1)
p26 = [1]*(k+1)

for i in range(k):
  p25[i+1] = p25[i]*25%mod
  p26[i+1] = p26[i]*26%mod

ans = 0
for p in range(k+1):
  chk = p25[p]*comb(L-1+p,L-1)%mod
  chk *= p26[k-p]%mod
  ans += chk
  ans %= mod
  
print(ans)
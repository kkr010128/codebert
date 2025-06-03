import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
mod = 10 ** 9 +7
    
K = int(readline())
S = readline().decode().rstrip()
s = len(S)-1

n = s+K
fact = [1] * (n+1)
fact_inv = [1] * (n+1)
for i in range(1,n+1):
    fact[i] = fact[i-1] * i % mod 
fact_inv[n] = pow(fact[n],mod-2,mod)
for i in range(n,0,-1):
    fact_inv[i-1] = (i * fact_inv[i]) % mod 

def comb(n,r):
  return fact[n] * fact_inv[r] * fact_inv[n-r] % mod

ans = 0
for i in range(K+1):
    ans += (comb(i+s,s) * pow(25,i,mod) % mod * pow(26,K-i,mod)) % mod
print(ans%mod)
mod = pow(10,9)+7
N,K = map(int,input().split())

A = sorted(list(map(int,input().split())))
B = A[::-1]
n= N

fac = [1]*(n+1)
inv = [1]*(n+1)
for i in range(1,n+1):
  fac[i] = (fac[i-1]*i) % mod  
inv[n] = pow(fac[n], mod-2, mod)
for i in range(n, 0, -1):
  inv[i-1] = (inv[i]*i) % mod
    
def nCr(n,r):  
  if r < 1:
    return 1
  return (((fac[n] * inv[r])%mod) * inv[n-r]) % mod

counter_min=0
counter_max=0
for i in range(N-K+1): #i=0 1 2 
    counter_max += A[N-1-i] * nCr(N-1-i,K-1)
    counter_min += B[N-1-i] * nCr(N-1-i,K-1)

print((counter_max-counter_min)%mod)

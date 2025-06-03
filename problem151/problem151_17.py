#factorial
MOD = 998244353 
N = 1000000
modinv_t = [0, 1]
modfact_t = [1, 1]
modfactinv_t = [1, 1]
for i in range(2,N+1):
  modfact_t.append(modfact_t[-1] * i % MOD)
  modinv_t.append(modinv_t[MOD%i] * (MOD-(MOD//i)) % MOD)
  modfactinv_t.append(modfactinv_t[-1] * modinv_t[-1] % MOD)
# permutation
def nPr(n, r):
  return  modfact_t[n] * modfactinv_t[n-r] % MOD
# combination
def nCr(n, r):
  return  modfact_t[n] * modfactinv_t[n-r] * modfactinv_t[r] % MOD
#
def nHr(n, r):
  return  nCr(n+r-1,r)
#

N, M, K = map(int, input().split()) 

t = M*pow(M-1,N-1,MOD) % MOD
for i in range(1,K+1):
  t += M*pow(M-1,N-1-i,MOD)*nCr((N-1),i)
  t %= MOD
#
print(t)

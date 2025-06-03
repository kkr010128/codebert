import math
MAX=510000
fac=[0]*MAX
finv=[0]*MAX
inv=[0]*MAX
MOD=10**9+7
#テーブルを作る前処理
def COMinit():
    fac[0]=fac[1]=1
    finv[0]=finv[1]=1
    inv[1]=1
    for i in range(2,MAX):
      fac[i] = fac[i-1] * i % MOD
      inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
      finv[i] = finv[i - 1] * inv[i] % MOD

#二項係数計算
def comb(n,k):
  if (n < k):
    return 0
  if (n < 0 or k < 0):
    return 0
  else:
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

COMinit()
N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
#print(A)
sum=0
for i in range(N-K+1):
  sum+=(A[N-1-i]-A[i])*(comb(N-i-1,K-1))%(10**9+7)
print(sum%(10**9+7))
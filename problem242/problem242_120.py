# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 10**9+7
N,K = map(int,readline().split())
fact = [1] * (N+1)
fact_inv = [1] * (N+1)
for i in range(1,N+1):
    fact[i] = fact[i-1] * i % MOD 
fact_inv[N] = pow(fact[N],MOD-2,MOD)
for i in range(N,0,-1):
    fact_inv[i-1] = (i * fact_inv[i]) % MOD
### nCrの計算 
def comb(n,r):
  return fact[n] * fact_inv[r] * fact_inv[n-r] % MOD

A = list(map(int,readline().split()))
A = sorted(A)
n = N-1
k = K-1
i = 0
ans = 0
while n >= k:
    ans += comb(n,k) * (A[N-1-i]-A[i]) % MOD
    n -= 1 
    i += 1
print(ans%MOD)
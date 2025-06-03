def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n % m)

N = int(input())
A = list(map(int,input().split()))
mod = 10**9+7

kbs = A[0]
for i in range(1,N):
  kbs = kbs*A[i]//gcd(kbs,A[i])
kbs %= mod

ans = 0
for i in range(N):
  ans += pow(A[i],mod-2,mod)
  ans %= mod
print(kbs*ans%mod)    
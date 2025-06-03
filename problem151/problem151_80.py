n,m,k = map(int,input().split())

MOD = 998244353
FAC = [1]
INV = [1]
for i in range(1,n+1):
  FAC.append((FAC[i-1]*i) % MOD)
  INV.append(pow(FAC[-1],MOD-2,MOD))

def nCr(n,r):
  return FAC[n]*INV[n-r]*INV[r]

ans = 0
for i in range(k+1):
  ans += nCr(n-1,i)*m*pow(m-1,n-i-1,MOD)
  ans %= MOD
print(ans)
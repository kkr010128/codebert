n,k = map(int,input().split())
MOD = 10**9+7

FAC = [1]
INV = [1]
for i in range(1,2*n+1):
  FAC.append((FAC[i-1]*i) % MOD)
  INV.append(pow(FAC[-1],MOD-2,MOD))

def nCr(n,r):
  return FAC[n]*INV[n-r]*INV[r]

ans = 0
for i in range(min(n-1,k)+1):
  ans += nCr(n,i)*nCr(n-1,n-i-1)
  ans %= MOD
print(ans)

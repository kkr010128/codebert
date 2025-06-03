n,k = map(int,input().split())
MOD = 10**9+7
# g[i]:gcd(A1,A2,,,An)=iとなる数列の個数
g = [0 for _ in range(k)]
for i in range(k,0,-1):
  g[i-1] = pow(k//i,n,MOD)
  #ここまででg[x]=gcdがxの倍数となる数列の個数となっているので、
  #ここからgcdが2x,3x,,,となる数列の個数を引いていく。
  for j in range(2,k+1):
    if i*j > k:
      break
    g[i-1] -= g[i*j-1]
    g[i-1] %= MOD
#print(g)
ans = 0
for i in range(k):
  ans += (i+1)*g[i]
  ans %= MOD
print(ans)

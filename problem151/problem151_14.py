def combs_mod(n,k,mod):
  #nC0からnCkまで
  inv = [1]*(k+1)
  for i in range(1,k+1):
    inv[i] = pow(i,mod-2,mod)
  ans = [1]*(k+1)
  for i in range(1,k+1):
    ans[i] = ans[i-1]*(n+1-i)*inv[i]%mod
  return ans

def solve():
  ans = 0
  mod = 998244353
  N, M, K = map(int, input().split())
  lis = combs_mod(N-1,K,mod)
  for i in range(K+1):
    ans += M*lis[i]*pow(M-1,N-1-i,mod)
    ans %= mod
  return ans
print(solve())
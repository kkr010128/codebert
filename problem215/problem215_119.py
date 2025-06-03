class mod_comb_k():
  def __init__(self, MAX_N = 10**6, mod = 10**9+7):
    self.fact = [1]
    self.fact_inv = [0] * (MAX_N + 4)
    self.mod = mod
    for i in range(MAX_N + 3):
      self.fact.append(self.fact[-1] * (i + 1) % self.mod)
    self.fact_inv[-1] = pow(self.fact[-1], self.mod - 2, self.mod)
    for i in range(MAX_N + 2, -1, -1):
      self.fact_inv[i] = self.fact_inv[i + 1] * (i + 1) % self.mod
  def comb(self, n, k):
    if n < k:return 0
    else:return self.fact[n] * self.fact_inv[k] % self.mod * self.fact_inv[n - k] % self.mod
c=mod_comb_k()
n,k=map(int,input().split())
if k>=n:print(c.comb(2*n-1,n))
else:
  ans=0
  m=10**9+7
  for i in range(k+1):
    ans+=c.comb(n-1,i)*c.comb(n,i)%m
    ans%=m
  print(ans)
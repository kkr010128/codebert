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
a=sorted(list(map(int,input().split())))
ans=0
mod=10**9+7
for i,j in enumerate(a,1):
  ans-=j*c.comb(n-i,k-1)
  ans%=mod
for i,j in enumerate(a[::-1],1):
  ans+=j*c.comb(n-i,k-1)
  ans%=mod
print(ans)
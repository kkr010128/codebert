class UnionFind:
  par = None
  
  def __init__(self, n):
    self.par = [0] * n
    
  def root(self, x):
    if(self.par[x] == 0):
      return x
    else:
      self.par[x] = self.root(self.par[x])
      return self.root(self.par[x])
  
  def unite(self, x, y):
    if(self.root(x) != self.root(y)):
      self.par[self.root(x)] = self.root(y)
      
  def same(self, x, y):
    return self.root(x) == self.root(y)
  
N, M = list(map(int, input().split()))
UF = UnionFind(N)
for i in range(M):
  A, B = list(map(int, input().split()))
  UF.unite(A - 1, B - 1) 
ans = 0
for i in range(N):
  if(UF.par[i] == 0):
    ans += 1
print(ans - 1)  

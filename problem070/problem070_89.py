class UnionFind:
  def __init__(self, n):
    self.par = [i for i in range(n+1)]
    self.rank = [0] * (n+1)
 
    # 検索
  def find(self, x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]
 
  # 併合
  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if self.rank[x] < self.rank[y]:
      self.par[x] = y
    else:
      self.par[y] = x
      if self.rank[x] == self.rank[y]:
        self.rank[x] += 1
 
  # 同じ集合に属するか判定
  def same_check(self, x, y):
    return self.find(x) == self.find(y)
n,m = map(int,input().split())
u = UnionFind(n)
for _ in range(m):
  ai,bi = map(int,input().split())
  u.union(ai,bi)
s = [0 for _ in range(n+1)]
for i in range(1,n+1):
  s[u.find(i)] = 1
print(sum(s)-1)
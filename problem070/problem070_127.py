class UnionFind():
  def __init__(self, n):
    self.par = [i for i in range(n+1)]
    self.rank = [0] * (n+1)
    
  def find(self, x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]

  def unite(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if self.rank[x] < self.rank[y]:
      self.par[x] = y
    else:
      self.par[y] = x
      
    if self.rank[x] == self.rank[y]:
      self.rank[x] += 1

  def same(self, x, y):
    return self.find(x) == self.find(y)

N,M=map(int,input().split())
city=UnionFind(N)

for i in range(M):
  A,B=map(int,input().split())
  city.unite(A,B)

ck=[0]*(N+10)
for i in range(1,N+1):
  root=city.find(i)
  if ck[root]==0:
    ck[root]=1
    
#print(city.par)
#print(ck)
    
Ans=sum(ck)-1
print(Ans)

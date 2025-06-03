class UnionFind():
  def __init__(self,n):
    self.n=n
    self.root=[-1]*(n+1)
    self.rank=[0]*(n+1)
  def FindRoot(self,x):
    if self.root[x]<0:
      return x
    else:
      self.root[x]=self.FindRoot(self.root[x])
      return self.root[x]
  def Unite(self,x,y):
    x=self.FindRoot(x)
    y=self.FindRoot(y)
    if x==y:
      return
    else:
      if self.rank[x]>self.rank[y]:
        self.root[x]+=self.root[y]
        self.root[y]=x
      elif self.rank[x]<=self.rank[y]:
        self.root[y]+=self.root[x]
        self.root[x]=y
        if self.rank[x]==self.rank[y]:
          self.rank[y]+=1
  def isSameGroup(self,x,y):
    return self.FindRoot(x)==self.FindRoot(y)
  def Count(self,x):
    return -self.root[self.FindRoot(x)]

n,m=map(int,input().split())
uf=UnionFind(n+1)
for _ in range(m):
  a,b=map(int,input().split())
  uf.Unite(a,b)
s=set()
for i in range(1,n+1):
  s.add(uf.FindRoot(i))
print(len(s)-1)
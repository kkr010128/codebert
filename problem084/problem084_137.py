class UF():
  def __init__(self, N):
    self._parent=[n for n in range(0, N)]
    self._size=[1] * N

  def find_root(self, x):
    if self._parent[x]==x:return x
    self._parent[x]=self.find_root(self._parent[x])
    return self._parent[x]

  def unite(self, x, y):
    gx=self.find_root(x)
    gy=self.find_root(y)
    if gx==gy:return

    if self._size[gx]<self._size[gy]:
      self._parent[gx]=gy
      self._size[gy]+=self._size[gx]
    else:
      self._parent[gy]=gx
      self._size[gx]+=self._size[gy]

  def size(self, x):
    return self._size[self.find_root(x)]

  def samegroup(self, x, y):
    return self.find_root(x)==self.find_root(y)

  def groupnum(self):
    N=len(self._parent)
    ans=0
    for i in range(N):
      if self.find_root(i)==i:
        ans+=1
    return ans

n,m=map(int,input().split())
UFa=UF(n)
for i in range(m):
  x,y=map(int,input().split())
  UFa.unite(x-1,y-1)
ans=[]
for i in range(n):
  ans.append(UFa.size(i))
print(max(ans))
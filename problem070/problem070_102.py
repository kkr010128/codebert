class UnionFind:
  def __init__(self, n):
    self.n = [-1]*n
    self.r = [0]*n
    self.co = n

  def find(self, x):
    if self.n[x] < 0:
      return x
    else:
      self.n[x] = self.find(self.n[x])
      return self.n[x]

  def unite(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x == y:
      return
    elif self.r[x] > self.r[y]:
      self.n[x] += self.n[y]
      self.n[y] = x
    else:
      self.n[y] += self.n[x]
      self.n[x] = y
      if self.r[x] == self.r[y]:
        self.r[y] += 1
    self.co -= 1

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def size(self, x):
    return -self.n[self.find(x)]

  def set_count(self):
    return self.co

n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
  a, b = map(int, input().split())
  uf.unite(a-1, b-1)
print(uf.set_count()-1)

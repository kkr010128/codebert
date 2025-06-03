class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

# class UnionFind():
#   par = []
#   sizes = []

#   def __init__(self, N):
#     self.par = [i for i in range(N)]
#     self.sizes = [1 for _ in range(N)]

#   def root(self, x: int)-> int:
#     if (self.par[x] == x):
#       return x
#     return self.root(self.par[x])

#   def unite(self, x: int, y: int):
#     rootX = self.root(x)
#     rootY = self.root(y)
#     if rootX == rootY:
#       return
#     self.par[rootX] = rootY
#     self.sizes[rootY] += self.sizes[rootX]

#   def maxSize(self)-> int:
#     return max(self.sizes)

def friends(N, As):
  uf = UnionFind(N)
  setAs = list(set(As))
  for val in setAs:
    uf.union(val[0]-1, val[1]-1)
  ans = 0
  for i in range(N):
    temp = uf.size(i)
    if ans < temp:
      ans = temp
  return ans

if __name__ == "__main__":
  nm = list(map(int, input().split()))
  As =[tuple(map(int, input().split())) for _ in range(nm[1])]
  print(friends(nm[0], As))
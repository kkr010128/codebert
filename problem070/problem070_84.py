from collections import Counter
N, M = map(int, input().split())
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]

    def unite(self, x, y):
        if not self.same(x, y):
            self.root[self.find(y)] = self.find(x)

    def find(self, x):
        if x == self.root[x]:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)
UF = UnionFind(N)
ans = N-1
for _ in range(M):
  x, y = map(int, input().split())
  if not UF.same(x-1, y-1):
    UF.unite(x-1, y-1)
    ans -= 1
print(ans)
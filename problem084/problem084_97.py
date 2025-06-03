n, m = map(int, input().split())

class UnionFind:
    def __init__(self, n):
        self.pare = [-1] * n
        self.size = [1] * n
    def root(self, x):
        if self.pare[x] < 0:
            return x
        r = self.root(self.pare[x])
        self.pare[x] = r
        return r
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        self.pare[rx] = ry
        self.size[ry] += self.size[rx]
        return

uf = UnionFind(n)

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    uf.unite(a, b)

print(max(uf.size))
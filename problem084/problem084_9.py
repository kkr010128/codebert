class UnionFind():
    def __init__(self, n):
        self.r = [-1 for _ in range(n)]

    def root(self, x):
        if self.r[x] < 0:
            return x
        self.r[x] = self.root(self.r[x])
        return self.r[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.r[x] > self.r[y]:
            x, y = y, x
        self.r[x] += self.r[y]
        self.r[y] = x
        return True

    def size(self, x):
        return -self.r[self.root(x)]


n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    uf.unite(a - 1, b - 1)

max_friend = -min(uf.r)

print(max_friend)
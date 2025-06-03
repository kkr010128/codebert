class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = list(range(self.n))
        self.rank = [1] * n
        self.cnt = n
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def unite(self, x, y):
        p = self.find(x)
        q = self.find(y)
        if p == q:
            return None
        if p > q:
            p, q = q, p
        self.rank[p] += self.rank[q]
        self.par[q] = p
        self.cnt -= 1
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def size(self, x):
        return self.rank[x]
    def count(self):
        return self.cnt
n, m = map(int, input().split())
UF = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    UF.unite(a - 1, b - 1)
print(UF.count() - 1)
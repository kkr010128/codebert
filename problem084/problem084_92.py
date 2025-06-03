import sys
from collections import Counter


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

class UnionFind():
    def __init__(self, n):
        self.n = n                              # 要素数(初期頂点数)
        self.root = [i for i in range(n)]       # 根
        self.rank = [0] * n                     # 深さ
        self.sizes = [1] * n                     # 要素数(木)

    def find(self, x):                          # 根を返す
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])  # 経路圧縮
        return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:         # 浅い方を深い方につなげる
            self.root[x] = y
            self.sizes[y] += self.sizes[x]
        else:
            self.root[y] = x
            self.sizes[x] += self.sizes[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):                       # 同じ集合かどうかの真偽を返す
        return self.find(x) == self.find(y)

    def roots(self):
        return {i for i, num in enumerate(self.root) if i == num}

    def size(self, x):
        return self.sizes[self.find(x)]

n, m = inintm()

uf = UnionFind(n)

for i in range(m):
    a, b = inintm()
    uf.unite(a-1, b-1)

ans = 0

r = uf.roots()

for i in r:
    if uf.size(i) > ans:
        ans = uf.size(i)

print(ans)

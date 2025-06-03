import sys

class UnionFind():
    def __init__(self, n):
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


N, M = map(int, input().split())
info = [()] * M
for i in range(M):
    info[i] = map(int, input().split())

uf = UnionFind(N)
for a, b in info:
    a -= 1; b -= 1
    uf.union(a, b)

ans = min(uf.parents)

print(-ans)
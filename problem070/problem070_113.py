class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.parents[x] = y
        else:
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

n, m = map(int, input().split())

uf = UnionFind(n)

for _ in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    uf.union(x, y)

for i in range(n):
    uf.find(i)

print(len(set(uf.parents))-1)
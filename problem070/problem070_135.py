class UnionFind:
    def __init__(self, n=1):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.parent[y] = x
    
    def is_same(self, x, y):
        return self.find(x) == self.find(y)


N, M = map(int, input().split())
uf = UnionFind(N)
for i in range(M):
    a, b = map(int, input().split())
    uf.union(a-1, b-1)

for i in range(N):
    uf.find(i)

print(len(set([uf.find(i) for i in range(N)])) - 1)
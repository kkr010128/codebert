class UnionFind:
    def __init__(self, n: int) -> None:
        self.forest = [-1] * n

    def union(self, x: int, y: int) -> None:
        x = self.findRoot(x)
        y = self.findRoot(y)
        if x == y:
            return
        if self.forest[x] > self.forest[y]:
            x,y = y,x
        self.forest[x] += self.forest[y]
        self.forest[y] = x
        return

    def findRoot(self, x: int) -> int:
        if self.forest[x] < 0:
            return x
        else:
            self.forest[x] = self.findRoot(self.forest[x])
            return self.forest[x]

    def issame(self, x: int, y: int) -> bool:
        return self.findRoot(x) == self.findRoot(y)

    def size(self,x: int) -> int:
        return -self.forest[self.findRoot(x)]


n,m = map(int,input().split())
uf = UnionFind(n)
s = set()
for i in range(m):
    ai,bi = map(int,input().split())
    uf.union(ai-1,bi-1)

for i in range(n):
    s.add(uf.findRoot(i))
print(len(s)-1)
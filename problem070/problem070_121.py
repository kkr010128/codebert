import sys
sys.setrecursionlimit(10 ** 9)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):#親となる要素を探索
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])#再帰
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        elif self.rank[x] > self.rank[y]:#深い木に連結
            self.root[x] += self.root[y]
            self.root[y] = x#yの親をxとする

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def issame(self, x, y):#x, yが同じ集合か判定
            return self.find(x) == self.find(y)


    def count(self, x):#要素の個数
        return (-1)*self.root[self.find(x)]

n, m = map(int, input().split())
uf = UnionFind(n)

for i in range(m):
    a, b = map(int, input().split())
    uf.unite(a-1, b-1)

ans = set()

for i in range(n):
    ans.add(uf.find(i))

print(len(ans)-1)
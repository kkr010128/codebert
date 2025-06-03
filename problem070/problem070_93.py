#0926
class UnionFind(): # 0インデックス
    def __init__(self, n):
        self.n = n
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

    def size(self, x):
        return -self.parents[self.find(x)]
    
    def test(self):
        return self.parents
    def test2(self):
        return sum(z <0 for z in self.parents)
    
N, M = map(int, input().split()) # N人、M個の関係
uf = UnionFind(N)
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    uf.union(A, B)
    
print(uf.test2()-1)
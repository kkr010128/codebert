N,M=map(int, input().split())

class UnionFind():
    def __init__(self, n):
        self.n = n # ノード数
        self.parents = [-1]*n # 各ノードごとのparent

    def find(self, x):
        # 自身が根であれば
        if self.parents[x]<0:
            return x
        # そうでなければ、再帰的に繰り返し、自身の根を探索
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        # それぞれの根
        x = self.find(x)
        y = self.find(y)

        # 根が同一であれば
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x,y = y,x
        self.parents[x]+=self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

uf = UnionFind(N)
for _ in range(M):
    i, j = map(int, input().split())
    i-=1
    j-=1
    uf.union(i,j)

max_size = 0
for i in range(N):
    if uf.parents[i]<0:
        size = uf.size(i)
        if max_size<size:
            max_size = size
print(max_size)

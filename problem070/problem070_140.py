(N,M),*AB=[list(map(int, x.split())) for x in open(0).readlines() if len(x)>1]

class UnionFind:
    def __init__(self, n):
        self.n=n
        self.parents=[-1 for i in range(n)]

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.parents[rx] > self.parents[ry]:
            rx,ry=ry,rx
        self.parents[rx] = self.parents[ry]
        self.parents[ry] = rx

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i,x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


d=UnionFind(N)
for a,b in AB:
    d.union(a-1,b-1)
print(d.group_count() - 1)
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

class Union:
    def __init__(self, n):
        self.parents = [-1] * n
    
    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            return self.root(self.parents[x])
    
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

uni = Union(n)
for a, b in ab:
    uni.unite(a-1, b-1)
print(-min(uni.parents))
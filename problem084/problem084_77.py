from copy import deepcopy

N, M = map(int, input().split())

pairs = [0] * M
for i in range(M):
    pairs[i] = list(map(int, input().split()))


# N = 5
# pairs = [[1,2], [3,4], [5,1]]


class UnionFind:
    def __init__(self, N):
        self.r = [-1] * N

    def root(self, x):
        if self.r[x] < 0:
            return x
        self.r[x] = self.root(self.r[x])
        return self.r[x]


    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.r[x] > self.r[y]:
            x, y = y, x

        self.r[x] += self.r[y]
        self.r[y] = x
        return True

    def size(self, x):
        return -self.r[self.root(x)]

uf = UnionFind(N)
for pair in pairs:
    a = pair[0] - 1
    b = pair[1] - 1
    uf.unite(a, b)

ans = 0
for i in range(N):
    ans = max(ans, uf.size(i))

print(ans)

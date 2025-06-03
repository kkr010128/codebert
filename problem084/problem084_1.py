class Unionfind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def root (self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def connect(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def isConnect(self, x):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parents[self.root(x)]

N, M = map(int, input().split())
uf = Unionfind(N)
for i in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    uf.connect(a, b)
ans = 0
for i in range(N):
    ans = max(ans, uf.size(i))
print(ans)

import sys
input = sys.stdin.readline

class UnionFind():
    def __init__(self, N):
        self.N = N
        self.r = [-1] * (N+1)

    def root(self, x):
        if (self.r[x] < 0):
            return x
        else:
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

    def same(self, x, y):
        return self.root(x) == self.root(y)

def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for _ in range(M):
        A, B = map(lambda i: int(i)-1, input().split())
        uf.unite(A, B)

    ans = 0
    for i in range(N):
        ans = max(ans, uf.size(i))

    print(ans)

main()
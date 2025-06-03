class UnionFind:
    def __init__(self, sz: int):
        self._par: list[int] = [-1] * sz

    def root(self, a: int):
        if self._par[a] < 0:
            return a
        self._par[a] = self.root(self._par[a])
        return self._par[a]
    
    def size(self, a: int):
        return -self._par[self.root(a)]
    
    def unite(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a != b:
            if self.size(a) < self.size(b):
                a, b = b, a
            self._par[a] += self._par[b]
            self._par[b] = a
    
if __name__ == '__main__':
    N, M = map(int, input().split())
    uf = UnionFind(N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        uf.unite(a, b)
    ans = 1
    for i in range(1, N + 1):
        ans = max(ans, uf.size(i))
    print(ans)
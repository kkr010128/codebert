n, m = map(int, input().split())


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [int(x) for x in range(n)]
        self.tree_size = [1 for _ in range(n)]

    def unite(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.same(x_root, y_root):
            return

        if self.size(x_root) >= self.size(y_root):
            self.parent[y_root] = x_root
            self.tree_size[x_root] += self.tree_size[y_root]
        else:
            self.parent[x_root] = y_root
            self.tree_size[y_root] += self.tree_size[x_root]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def size(self, x):
        return self.tree_size[self.find(x)]

    def same(self, x, y):
        if x == y:
            return True
        else:
            return False


uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    uf.unite(a-1, b-1)

# print([uf.size(i) for i in range(n)])
print(max([uf.size(i) for i in range(n)]))

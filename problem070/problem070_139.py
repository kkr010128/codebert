class UnionFind:
    def __init__(self, num):
        self.parent = [-1] * num

    def find(self, node):
        if self.parent[node] < 0:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        node1 = self.find(node1)
        node2 = self.find(node2)
        if node1 == node2:
            return
        if self.parent[node1] > self.parent[node2]:
            node1, node2 = node2, node1
        self.parent[node1] += self.parent[node2]
        self.parent[node2] = node1
        return

    def same(self, node1, node2):
        return self.find(node1) == self.find(node2)

    def size(self, x):
        return -self.parent[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.parent) if x < 0]

    def group_count(self):
        return len(self.roots())


n, m = map(int, input().split())

uf = UnionFind(n)

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    uf.union(a, b)

print(uf.group_count() - 1)


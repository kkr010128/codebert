class UnionFind:
    def __init__(self):
        self.data = {}
        self.heights = {}
        self.sizes = {}

    def get_num_trees(self):
        return len(self.heights)

    def get_tree_size(self, a):
        return self.sizes[self.get_root(a)]

    def add_node(self, a):
        self.data[a] = a
        self.heights[a] = 1
        self.sizes[a] = 1

    def get_root(self, a):
        nodes = [a]
        while nodes[-1] not in self.heights:
            nodes.append(self.data[nodes[-1]])
        for x in nodes:
            self.data[x] = nodes[-1]
        return nodes[-1]

    def union(self, a, b):
        root_a = self.get_root(a)
        root_b = self.get_root(b)
        if root_a == root_b:
            return
        if self.heights[root_a] > self.heights[root_b]:
            a, b = b, a
            root_a, root_b = root_b, root_a
        self.data[root_a] = root_b
        self.heights[root_b] = max(self.heights.pop(root_a) + 1, self.heights[root_b])
        self.sizes[root_b] += self.sizes.pop(root_a)

    def find(self, a, b):
        return self.get_root(a) == self.get_root(b)


N, M = map(int, input().split())
uf = UnionFind()
for i in range(1, N + 1):
    uf.add_node(i)

for _ in range(M):
    A, B = map(int, input().split())
    uf.union(A, B)

print(max(uf.sizes.values()))
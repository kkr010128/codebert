class Tree():
    def __init__(self, n, edge, indexed=1):
        self.n = n
        self.tree = [[] for _ in range(n)]
        for e in edge:
            self.tree[e[0] - indexed].append(e[1] - indexed)
            self.tree[e[1] - indexed].append(e[0] - indexed)

    def setroot(self, root):
        self.root = root
        self.parent = [None for _ in range(self.n)]
        self.parent[root] = -1
        self.depth = [None for _ in range(self.n)]
        self.depth[root] = 0
        self.order = []
        self.order.append(root)
        self.size = [1 for _ in range(self.n)]
        stack = [root]
        while stack:
            node = stack.pop()
            for adj in self.tree[node]:
                if self.parent[adj] is None:
                    self.parent[adj] = node
                    self.depth[adj] = self.depth[node] + 1
                    self.order.append(adj)
                    stack.append(adj)
        for node in self.order[::-1]:
            for adj in self.tree[node]:
                if self.parent[node] == adj:
                    continue
                self.size[node] += self.size[adj]

import sys
input = sys.stdin.readline

N, u, v = map(int, input().split())
u -= 1; v -= 1
E = [tuple(map(int, input().split())) for _ in range(N - 1)]

t = Tree(N, E)
t.setroot(u); dist1 = t.depth
t.setroot(v); dist2 = t.depth

tmp = 0
for i in range(N):
    if dist1[i] < dist2[i]:
        tmp = max(tmp, dist2[i])

print(tmp - 1)
# coding: utf-8
# Your code here!
class UnionFind:
    def __init__(self, size):
        self.rank = [0 for i in range(size)]
        self.parent = [-1 for i in range(size)]
        self.children = [[i] for i in range(size)]
    
    def Find(self, x):
        parent = self.parent[x]
        while parent >= 0:
            x = parent
            parent = self.parent[x]
        return x
    
    def Union(self, x, y):
        root_x = self.Find(x)
        root_y = self.Find(y)
        if root_x == root_y:
            return
        else:
            if self.rank[root_x] >= self.rank[root_y]:
                self.parent[root_x] += self.parent[root_y]
                self.parent[root_y] = root_x
                self.rank[root_x] = max(self.rank[root_y] + 1, self.rank[root_x])
                self.children[root_x] += self.children[root_y]
            else:
                self.parent[root_y] += self.parent[root_x]
                self.parent[root_x] = root_y
                self.rank[root_y] = max(self.rank[root_x] + 1, self.rank[root_y])
                self.children[root_y] += self.children[root_x]
    def Same(self, x, y):
        return self.Find(x) == self.Find(y)
    def FindRootAndSizeAndChildren(self):
        return [(idx, -val, self.children[idx]) for idx, val in enumerate(self.parent) if val<0 ]
    def print_lists(self):
        print(self.rank)
        print(self.parent)
        print()


N, M = map(int, input().split())
unionfind = UnionFind(N)
for i in range(M):
    a, b = map(int, input().split())
    unionfind.Union(a-1, b-1)

max_size = 0
for idx, size, children in unionfind.FindRootAndSizeAndChildren():
    if size > max_size:
        max_size = size
print(max_size)

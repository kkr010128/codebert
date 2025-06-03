class UnionFind:

    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
            
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x    

N, M = map(int, input().split())
uf = UnionFind(N)

for i in range(M):
    a,b = map(int, input().split())
    uf.union(a-1,b-1)

ans = 0
for i in range(N):
    ans = max(ans, -uf.parents[i])
print(ans)    
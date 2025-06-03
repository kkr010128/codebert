class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x==y:
            return False

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

    def size(self, x):
        return -self.parents[self.find(x)]

N, M = map(int, input().split())
ans = 0

UF = UnionFind(N)

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    UF.union(a,b)

for i in range(N):
    ans = max(ans, UF.size(i))

print(ans)
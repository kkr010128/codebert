#self.r[x] means root of "x" if "x" isn't root, else number of elements
class UnionFind():
    def __init__(self, n):
        self.r = [-1 for i in range(n)]
    
    #use in add-method
    def root(self, x):
        if self.r[x] < 0: #"x" is root
            return x
        self.r[x] = self.root(self.r[x])
        return self.r[x]

    #add new path
    def add(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        self.r[x] += self.r[y]
        self.r[y] = x
        return True

n, m = map(int, input().split())
UF = UnionFind(n)
for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    UF.add(a, b)

ans = 0
for i in UF.r:
    if i < 0:
        ans += 1

print(ans-1)

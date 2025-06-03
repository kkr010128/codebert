n,m = map(int,input().split())

ans = 0

class UnionFind:
    def __init__(self,n):
        self.root = [i for i in range(n+1)]

    def Root_Find(self,x):
        if self.root[x] == x:
            return x
        else:
            self.root[x] = self.Root_Find(self.root[x])
            return self.root[x]

    def Unite(self,x,y):
        x = self.Root_Find(x)
        y = self.Root_Find(y)
        if x == y:
            return
        self.root[y] = x

tree = UnionFind(n)

for i in range(m):
    a,b = map(int,input().split())
    tree.Unite(a,b)

for i in range(n+1):
    tree.Root_Find(i)

ans = len(list(set(tree.root))) - 2
print(ans)
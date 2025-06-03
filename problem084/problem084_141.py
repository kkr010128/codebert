class UnionFind:
    def __init__(self,n):
        self.par = {i:i for i in range(1,n+1)}
        self.rank = {i:0 for i in range(1,n+1)}
        self.size = {i:1 for i in range(1,n+1)}

    def find(self,x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self,x,y):
        px,py = self.find(x),self.find(y)
        res = 0
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.par[px] = py
                self.size[py] += self.size[px]
                res = self.size[py]
            else:
                self.par[py] = px
                self.size[px] += self.size[py]
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
                res = self.size[px]
        return res

n,m = map(int,input().split())
ans = 1
uf = UnionFind(n)
for _ in range(m):
    a,b = map(int,input().split())
    ans = max(ans,uf.union(a,b))
print(ans)
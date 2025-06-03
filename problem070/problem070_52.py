n,m = map(int, input().split())
#a = list(map(int, input().split()))

class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n)]
        self.siz=[1]*n

    def root(self,x):
        while self.par[x]!=x:
            self.par[x]=self.par[self.par[x]]
            x=self.par[x]
        return x

    def unite(self,x,y):
        x=self.root(x)
        y=self.root(y)
        if x==y:
            return False
        if self.siz[x]<self.siz[y]:
            x,y=y,x
        self.siz[x]+=self.siz[y]
        self.par[y]=x
        return True

    def is_same(self,x,y):
        return self.root(x)==self.root(y)

    def size(self,x):
        return self.siz[self.root(x)]

uni = UnionFind(n)
for i in range(m):
    a,b = map(int, input().split())
    uni.unite(a-1, b-1)

cnt = [0]*(n)
for i in range(n):
    cnt[uni.root(i)] = 1

print(sum(cnt)-1)
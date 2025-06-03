from collections import Counter

class UnionFind:
    def __init__(self,num:int):
        self.r = [-1 for i in range(num)]
    def root(self,x:int):
        if(self.r[x] < 0):
            return x
        self.r[x] = self.root(self.r[x])
        return self.r[x]
    def unite(self,x:int,y:int):
        rx = self.root(x)
        ry = self.root(y)
        if(rx == ry):
            return False
        if(self.r[rx] > self.r[ry]):
            rx,ry = ry,rx
        self.r[rx] += self.r[ry]
        self.r[ry] = rx
        return True
    def size(self,x:int):
        return -self.r[self.root(x)]

N,M = map(int,input().split())
group = UnionFind(N)
for i in range(M):
    A,B = map(int,input().split())
    group.unite(A-1,B-1)
ans = 0
for i in range(N):
    ans = max(ans,group.size(i))
print(ans)

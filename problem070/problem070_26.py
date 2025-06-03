class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0]*(n+1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)


N, M = map(int, input().split())
A = [0]*M
B = [0]*M
uf = UnionFind(N)
for i in range(M):
    A[i], B[i] = map(int, input().split())
    uf.union(A[i], B[i])

cnt = 0 #新しく作った橋の数

for j in range(1,N):
    if uf.same_check(j, j+1) == False:
        uf.union(j,j+1)
        cnt+=1

print(cnt)
#print(uf.par[1:])
#print(uf.rank[1:])
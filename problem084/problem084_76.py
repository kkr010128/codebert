class UnionFind():

    def __init__(self, N):
        # parent of each node
        self.parent = [n for n in range(N)]

        # number of nodes in union
        self.rank = [1] * N
        
    def find(self, u):
        if self.parent[u] == u:
            return u
        else:
            # recursive call
            return self.find(self.parent[u])
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        # same union
        if pu == pv: 
            return

        # let pv join into pu union 
        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu

        self.rank[pu] += self.rank[pv]
        self.parent[pv] = pu
 
N, M = map(int, input().split())
UF = UnionFind(N)
for _ in range(M):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    UF.union(A, B)


ret = 0

for n in range(N):
    ret = max(ret, UF.rank[n])

print(ret)

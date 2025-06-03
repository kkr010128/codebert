N,M,L = map(int,input().split())
ABC = [list(map(int,input().split())) for _ in range(M)]
Q = int(input())

class WarshallFloyd:
    def __init__(self,n):
        self.n = n
        self.inf = 100000000000000
        self.d = [[self.inf for _ in range(n)] for _ in range(n)]
        for i in range(self.n):
            self.d[i][i] = 0
    def register(self,v1,v2,l,multiple=True):
        self.d[v1][v2] = l
        if multiple:
            self.d[v2][v1] = l
    
    def solve(self):
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    self.d[j][k] = min(self.d[j][k],self.d[j][i]+self.d[i][k])
        return self.d

W = WarshallFloyd(N)
for a,b,c in ABC:
    W.register(a-1,b-1,c)
D = W.solve()

WL = WarshallFloyd(N)
for i in range(N):
    for j in range(N):
        if D[i][j] <= L and i != j:
            WL.register(i,j,1)
DL = WL.solve()
ST = [list(map(int,input().split())) for _ in range(Q)]
for i in range(Q):
    s,t = ST[i]
    transition = DL[s-1][t-1]
    if transition == 100000000000000:
        print(-1)
    else:
        print(transition-1)
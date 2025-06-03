import sys
input = sys.stdin.readline

class WarshallFloyd:
    def __init__(self,n):
        self.v = n
        self.d = [[1e100]*n for _ in range(n)]
        for i in range(n):
            self.d[i][i] = 0

    def path(self,x,y,c):
        if x == y:
            return False
        self.d[x][y] = c
        self.d[y][x] = c
        return True

    def build(self):
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])

n,m,l = map(int,input().split())
wf = WarshallFloyd(n)
for i in range(m):
    a,b,c = map(int,input().split())
    wf.path(a-1,b-1,c)
wf.build()
d = [[1e100]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            d[i][j] = 0
        elif wf.d[i][j] <= l:
            d[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

q = int(input())
for i in range(q):
    s,t = map(int,input().split())
    ans = d[s-1][t-1]
    if ans == 1e100:
        print(-1)
    else:
        print(ans - 1)

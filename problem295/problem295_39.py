import sys
input = sys.stdin.readline

N,M,L = map(int,input().split())
ABC = [list(map(int,input().split())) for _ in [0]*M]
Q = int(input())
ST = [list(map(int,input().split())) for _ in [0]*Q]


INF = (L+1)*N
d = [[INF]*N for _ in [0]*N]
for i in range(N):
    d[i][i] = 0
for a,b,c in ABC:
    a-=1;b-=1
    d[a][b] = c
    d[b][a] = c

def Warshall_Floyd(d,N=None):
    if N==None : N = len(d)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])

Warshall_Floyd(d,N)

d2 = [None]*N
for i,row in enumerate(d):
    d2[i] = [1 if e<=L else INF for e in row]
    d2[i][i] = 0

Warshall_Floyd(d2,N)

for s,t in ST:
    s-=1;t-=1
    ans = (d2[s][t]%INF)-1
    print(ans)
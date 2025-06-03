import sys
input = sys.stdin.readline

n,m,l = map(int,input().split())
town = [list(map(int,input().split())) for _ in range(m)]
q = int(input())
query = [list(map(int,input().split())) for _ in range(q)]

inf = (l+1)*n
d = [[inf]*n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for a,b,c in town:
    a -= 1
    b -= 1
    d[a][b] = c
    d[b][a] = c
    
def warshall_floyd(d,n):
    for k in range(n):
        for j in range(n):
            for i in range(n):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])

warshall_floyd(d,n)

d2 = [None]*n
for i,row in enumerate(d):
    d2[i] = [1 if val<=l else inf for val in row]
    d2[i][i] = 0

warshall_floyd(d2,n)
 
for s,t in query:
    s -= 1
    t -= 1
    count = (d2[s][t]%inf)-1
    print(count)

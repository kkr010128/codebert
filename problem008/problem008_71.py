n = int(raw_input())
 
d = [0 for i in range(n)]
f = [0 for i in range(n)]
G = [0 for i in range(n)]
M = [[0 for i in range(n)] for j in range(n)]
col = [0 for i in range(n)]
t = [0]
 
def DFS_visit(u):
    col[u] = 1
    t[0] += 1
    d[u] = t[0]
    for v in range(n):
        if M[u][v] == 1 and col[v] == 0:
            DFS_visit(v)
    col[u] = 2
    t[0] += 1
    f[u] = t[0]
 
def DFS():
    for u in range(n):
        if col[u] == 0:
            DFS_visit(u)
    for u in range(n):
        print'{0} {1} {2}'.format(u+1, d[u], f[u])
     
for i in range(n):
    X = map(int, raw_input().split())
    for j in range(X[1]):
        M[X[0]-1][X[2+j]-1] = 1
 
DFS()
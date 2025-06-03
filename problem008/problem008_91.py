n = int(raw_input())

d = [0 for i in range(n)]
f = [0 for i in range(n)]
G = [0 for i in range(n)]
M = [[0 for i in range(n)] for j in range(n)]
st = [0 for i in range(n)]
t = [0]

def DFS_visit(s):
    st[s] = 1
    t[0] += 1
    d[s] = t[0]
    for e in range(n):
        if M[s][e] == 1 and st[e] == 0:
            DFS_visit(e)
    st[s] == 2
    t[0] += 1
    f[s] = t[0]

def DFS():
    for s in range(n):
        if st[s] == 0:
            DFS_visit(s)
    for s in range(n):
        print'{0} {1} {2}'.format(s+1, d[s], f[s])
    
for i in range(n):
    G = map(int, raw_input().split())
    for j in range(G[1]):
        M[G[0]-1][G[2+j]-1] = 1

DFS()
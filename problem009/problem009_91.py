n = int(raw_input())
 
d = [99999 for i in range(n)]
G = [0 for i in range(n)]
M = [[0 for i in range(n)] for j in range(n)]
 
def BFS(s):
    for e in range(n):
        if M[s][e] == 1:
            if d[e] > d[s] + 1:
                d[e] = d[s]+1
                BFS(e)
 
for i in range(n):
    G = map(int, raw_input().split())
    for j in range(G[1]):
        M[G[0]-1][G[2+j]-1] = 1
 
d[0] = 0
for s in range(n):
        BFS(s)
for s in range(n):
    if d[s] == 99999:
        d[s] = -1
for s in range(n):
    print'{0} {1}'.format(s+1, d[s])
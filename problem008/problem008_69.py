N = int(input())
Adj = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    u = list(map(int, input().split()))
    if u[1] > 0:
        for k in u[2: 2+u[1]]:
            Adj[u[0] - 1][k - 1] = 1
            
            
color = [0] * N #1: visited, 0: not visited, 2: completed
s = [0] * N # start
f = [0] * N # finish

time = 0

def DFS(u):
    global time
    color[u-1] = 1
    time += 1
    s[u-1] = time
    
    for i in range(1, N+1):
        if Adj[u-1][i-1] == 1 and color[i-1] == 0:
            DFS(i)
            
    color[u-1] = 2
    time += 1
    f[u-1] = time

for i in range(1, N+1):
    if color[i-1] == 0:
        DFS(i)
        
for i in range(N):
    print('{} {} {}'.format(i+1, s[i], f[i]))
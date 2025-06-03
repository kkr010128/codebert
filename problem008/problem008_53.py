n = int(input())
Adj = [[0 for i in range(n)] for i in range(n)]
 
for i in range(n):
    u = list(map(int, input().split()))
    if u[1] > 0:
        for i in u[2: 2 + u[1]]:
            Adj[u[0] - 1][i - 1] = 1
 
color = [0] * n
d = [0] * n
f = [0] * n
time = 0
def dfs(u):
    global time
    color[u - 1] = 1
    time += 1
    d[u - 1] = time
    for i in range(1, n+1):
        if Adj[u - 1][i - 1] == 1 and color[i - 1] == 0:
            dfs(i)
    color[u - 1] = 2
    time += 1
    f[u - 1] = time

for i in range(1, n+1):
    if color[i-1] == 0:
        dfs(i)
for i in range(n):
    print("{} {} {}".format(i+1,d[i],f[i]))
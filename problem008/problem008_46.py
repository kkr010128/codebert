n = int(input())
graph = [[0 for i in range(n)] for j in range(n)]
d = [0] * n
f = [0] * n
g = [0] * n

time = 0

for i in range(n):
   a = list(map(int, input().split()))
   for j in range(0, a[1], 1):
       graph[a[0] - 1][a[2 + j] - 1] = 1

def search(i):
    global time
    time = time + 1
    d[i] = time
    g[i] = 1
    for j in range(n):
        if (graph[i][j] == 1) & (g[j] == 0):
            search(j)
    time = time + 1
    f[i] = time

for i in range(n):
    if g[i] == 0:
        search(i)
[print(i+1, d[i], f[i]) for i in range(n)]

n = int(input())
Adj = [[0]]
for _ in range(n):
    Adj.append(list(map(int, input().split()))[2:])

visited = [False]*(n+1)
s = [0]*(n+1)
f = [0]*(n+1)
time = 0

def dfs(i):
    global time
    time += 1
    s[i] = time
    visited[i] = True
    for j in Adj[i]:
        if not visited[j]:
            dfs(j)
    time += 1
    f[i] = time

while not all(visited[1:]):
    i = visited[1:].index(False) + 1
    dfs(i)

for i in range(1, n+1):
    print(i,s[i], f[i])

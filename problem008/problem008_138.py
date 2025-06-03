"""Depth First Search."""

n = int(input())

adj = [None]
for i in range(n):
    adj_i = list(map(int, input().split()[2:]))
    adj.append(adj_i)

# searched or not, number of vertex, discovery time and finishing time.
sndf = [None]
for i in range(1, n + 1):
    sndf.append([False, i])

path = []

time = 0

def dfs(u):
    global time
    path.append(u)
    sndf[u][0] = True
    time += 1
    sndf[u].append(time)

    while path:
        u = path[-1]
        if adj[u]:
            v = adj[u].pop(0)
            if not sndf[v][0]:
                sndf[v][0] = True
                time += 1
                sndf[v].append(time)
                path.append(v)
        else:
            path.pop()
            sndf[u][0] = True
            time += 1
            sndf[u].append(time)


for i in range(1, n + 1):
    if not sndf[i][0]:
        dfs(i)

for x in sndf[1:]:
    print(*x[1:])
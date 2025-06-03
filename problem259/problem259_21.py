n, u, v = map(int, input().split())
u, v = u-1, v-1
edges = [[] for i in range(n)]
for i in range(n-1):
    ai, bi = map(int, input().split())
    ai, bi = ai-1, bi-1
    edges[ai].append(bi)
    edges[bi].append(ai)

depth = 0
already = [0 for i in range(n)]
already[v] = 1
nodes = [v]
while nodes != []:
    depth += 1
    next_nodes = []
    for node in nodes:
        children = edges[node]
        for child in children:
            if already[child] == 0:
                already[child] = depth
                next_nodes.append(child)
    nodes = next_nodes
already[v] = 0

depth = 0
already_u = [0 for i in range(n)]
already_u[u] = 1
nodes = [u]
while nodes != []:
    depth += 1
    next_nodes = []
    for node in nodes:
        children = edges[node]
        for child in children:
            if already_u[child] == 0:
                already_u[child] = depth
                next_nodes.append(child)
    nodes = next_nodes
already_u[u] = 0

maxi = 0
for i in range(n):
    if already_u[i] < already[i]:
        maxi = max(maxi, already[i])

print(maxi-1)
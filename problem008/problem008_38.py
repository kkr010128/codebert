n = int(raw_input())

def dfs(u,t):
    global graph
    global found
    global timestamp

    if u in found: return t
    found.add(u)
    timestamp[u] = [-1,-1]
    timestamp[u][0] = t
    t += 1
    for v in graph[u]:
        t = dfs(v,t)
    timestamp[u][1] = t
    t += 1
    return t

graph = [[] for i in range(n)]
found = set()
timestamp = {}

for i in range(n):
    entry = map(int,raw_input().strip().split(' '))
    u = entry[0]
    u -= 1
    for v in entry[2:]:
        v -= 1
        graph[u].append(v)


t = 1
for i in range(n):
    t = dfs(i,t)

for i in timestamp:
    print i+1,timestamp[i][0],timestamp[i][1]
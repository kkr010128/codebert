j = 1

def dfs(graph, start, result, visited=None):
    global j
    if visited == None:
        visited = []
    visited.append(start)
    result[start][1]  = j
    for next in graph[start][2:]:
        if next in visited:
            continue
        j += 1
        dfs(graph, next, result, visited)
    else:
        j += 1
        result[start][2] = j

n = int(input())
g = [[]]
r = [[i,0,0] for i in range(n + 1)]
v = []

for i in range(n):
    g.append(list(map(int, input().split())))


for i in range(1, n + 1):
    if i in v:
        continue
    dfs(g,i,r,v)
    j += 1

for i in range(1,n+1):
    print(*r[i])
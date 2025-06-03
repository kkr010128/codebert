def bfs(graph, start, result):
    visited = {start: None}
    unvisited = [start]
    while unvisited:
        now = unvisited[0]
        unvisited = unvisited[1:]
        if visited[now] == None:
            result[now] = 0
        else:
            result[now] = result[visited[now]] + 1
        for next in graph[now][2:]:
            if not (next in visited):
                unvisited.append(next)
                visited[next] = now
    return visited

n = int(input())
g = [[]]
r = {i: -1 for i in range(n + 1)}

for i in range(n):
    g.append(list(map(int, input().split())))

v = bfs(g, 1, r)

for i in range(1,n+1):
    print(i, r[i])
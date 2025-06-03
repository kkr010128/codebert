n,m = list(map(int, input().split()))
graph = [set() for _ in range(n)]
for _ in range(m):
    a,b = list(map(int, input().split()))
    graph[a-1].add(b-1)
    graph[b-1].add(a-1)

stack = []
group = [-1] * n
gid = 0
i = 0
for i in range(n):
    if group[i] >= 0:
        continue
    group[i] = gid
    stack.append(i)
    while stack:
        current = stack.pop()
        for neighbor in graph[current]:
            if group[neighbor] == -1:
                group[neighbor] = gid
                stack.append(neighbor)
    gid += 1

print(gid-1)
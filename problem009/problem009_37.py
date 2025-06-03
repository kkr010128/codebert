from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
seen = [-1]*(N+1)

todo = deque()


def bfs(v):
    u = v-1
    next_v = graph[u][2:]
    for i in next_v:
        if seen[i] == -1:
            seen[i] = seen[v] + 1
            todo.append(i)


todo.append(1)
seen[1] = 0

while len(todo) > 0:
    bfs(todo.popleft())

for i in range(1, N+1):
    print(i, seen[i])

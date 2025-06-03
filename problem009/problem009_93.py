from collections import deque

def bfs(x):
  for v in graph[x]:
    if dist[v] != -1:
      continue
    dist[v] = dist[x] + 1
    queue.append(v)
  if len(queue) == 0:
    return
  bfs(queue.popleft())
  
N = int(input())
graph = []
for _ in range(N):
  graph.append(list(map(lambda x: int(x)-1, input().split()))[2:])
dist = [-1] * N
queue = deque()

dist[0] = 0
bfs(0)
for i in range(N):
  print("{} {}".format(i+1, dist[i]))

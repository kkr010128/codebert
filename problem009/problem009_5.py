import queue

n = int(input())
graph = {}
for _ in range(n):
  i = list(map(int,input().split()))
  graph[i[0]] = i[2:]

dist = [-1 for i in range(n)]
todo = queue.Queue()
seen = set()

dist[0] = 0
todo.put(1)

while (not todo.empty()):
  now = todo.get()
  for nx in graph[now]:
    if (dist[nx-1] != -1):
      continue
    dist[nx-1] = dist[now-1] + 1
    todo.put(nx)

for i in range(n):
  print(i+1, dist[i])



from collections import defaultdict, deque

V, E = map(int, input().split())

graph = defaultdict(dict)
for _ in range(E):
  a, b = map(int, input().split())
  graph[a][b] = True
  graph[b][a] = True

components = []				# list of components
visited = set()

for i in range(1, V+1):
  if i in visited:
    continue
  
  # do bfs starting from i
  current_component = set()
  queue = deque([i])
  visited.add(i)

  while queue:
    x = queue.popleft()
    
    current_component.add(x)
    
    for nbr in graph[x]:
      if nbr not in visited:
        queue.append(nbr)
        visited.add(nbr)
  
  components.append(current_component)

print(max(map(len, components)))
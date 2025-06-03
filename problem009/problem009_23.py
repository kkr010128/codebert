from collections import deque

N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
  X = list(map(int, input().split()))
  for j in range(2, len(X)):
    graph[i].append(X[j]-1)
    
dist = [-1] * N
dist[0] = 0

q = deque([])
q.append(0)

while q:
  x = q.popleft()
  for next_x in graph[x]:
    if(dist[next_x] > -1):
      continue
    dist[next_x] = dist[x] + 1
    q.append(next_x)
    
for i in range(N):
  print(i+1, dist[i])

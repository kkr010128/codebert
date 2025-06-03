import sys
sys.setrecursionlimit(10 ** 9)

N = int(input())
graph = list()
for i in range(N):
  x = list(map(int, input().split()))
  graph.append(x[2:])

start = [0] * N
end = [0] * N
visited = [False] * N
time = 0
def dfs(n):
  if visited[n]:
    return
  visited[n] = True
  global time
  time += 1
  start[n] = time
  for i in graph[n]:
    dfs(i-1)
  time += 1
  end[n] = time

for i in range(N):
  dfs(i)
for i in range(N):
  print(i+1, start[i], end[i])

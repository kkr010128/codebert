from enum import Enum

class Color(Enum):
  WHITE = 0
  GRAY = 1
  BLACK = 2

def dfs_visit(u, total_time):
  colors[u] = Color.GRAY
  total_time += 1
  d[u] = total_time
  stack.append(u)
  for v in range(N):
    if adj[u][v] == 1 and colors[v] == Color.WHITE:
      total_time = dfs_visit(v, total_time)
  colors[u] = Color.BLACK
  total_time += 1
  f[u] = total_time
  return total_time



def dfs(total_time):
  for i in range(N):
    if colors[i] != Color.WHITE:
      continue
    total_time = dfs_visit(i, total_time)

N = int(input())
L = [list(map(int, input().split())) for i in range(N)]
adj = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
  for node in L[i][2:]:
    adj[i][node-1] = 1

colors = [Color.WHITE for i in range(N)]
stack = []
total_time = 0
d = [0 for i in range(N)]
f = [0 for i in range(N)]

dfs(total_time)

for i in range(N):
  print(i+1, d[i], f[i])


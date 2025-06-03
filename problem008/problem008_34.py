from collections import defaultdict as dd

N = int(input())
graph = dd(list)
seen = dd(int)
u = []
d, f = dd(int), dd(int)
ts = 1
for _ in range(N):
  info = list(map(int, input().split()))
  u.append(info[0])
  graph[info[0]] = info[2:]

def dfs(v):
  global ts
  d[v] = ts
  ts += 1
  
  seen[v] = 1
  for next_v in graph[v]:
    if seen[next_v]:
      continue
    dfs(next_v)
  
  f[v] = ts
  ts += 1

for key in u:
  if seen[key]:
    continue
  dfs(key)

for id in u:
  print("{} {} {}".format(id, d[id], f[id]))

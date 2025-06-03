n = int(input())
graph = {}
for _ in range(n):
  i = list(map(int,input().split()))
  graph[i[0]] = i[2:]

first = {i:0 for i in range(1,n+1)}
last = {i:0 for i in range(1,n+1)}
seen = set()
time = 1

def dfs(v):
  global time
  seen.add(v)
  first[v] = time
  time += 1
  for nxt in graph[v]:
    if nxt in seen:
      continue
    dfs(nxt)
  last[v] = time
  time += 1

for i in range(1,n+1):
  if i not in seen:
    dfs(i)
  
for i in range(1,n+1):
  print(i, first[i], last[i])



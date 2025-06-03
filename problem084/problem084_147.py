n,m = map(int,input().split())
graph = [[] for i in range(n)]
for i in range(m):
  a,b = map(lambda z:int(z)-1,input().split())
  graph[a].append(b)
  graph[b].append(a)

size = [0 for i in range(n)]
check = [True for i in range(n)]
for i in range(n):
  if check[i]:
    tmp = 1
    stack = [i]
    check[i] = False
    while stack:
      now = stack.pop()
      size[now] = tmp
      tmp+=1
      for to in graph[now]:
        if check[to]:
          check[to] = False
          stack.append(to)

print(max(size))

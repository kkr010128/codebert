# coding: UTF-8
from collections import deque
#入力値の整理
n = int(input())
adj={}
visited={}
d={}
f={}
t=0
visited=set()
for i in range(n):
  raw=list(map(int,input().split()))
  u = raw.pop(0)
  k = raw.pop(0)
  raw.sort()
  q = deque(raw)
  adj[u] = q  
  d[u] = -1
  f[u] = -1

next = 1
v = next
d[next] = t + 1
stack = deque()
visited.add(v)

while True:
  t = t+1
  clear = True
  while adj[v]:
    cand = adj[v].popleft()
    if cand not in visited:
      next = cand
      d[next] = t + 1
      visited.add(next)
      clear = False
      break
  if clear:
    f[v] = t + 1
    if stack:
      next = stack.pop()
      v = next
    else:
      end = True
      for i in range(n):
        if i+1 not in visited:
          next = i+1
          end = False
          break
      if end:
        break
      else:
        t = t+1
        v = next
        d[next] = t + 1
        visited.add(v)
  else:
    stack.append(v)
    v = next

#print
i = 0
for j in range(n):
  i += 1
  print(str(i) + " " + str(d[i]) + " " + str(f[i]))

#return d,f


from collections import deque
n = int(input())
d = [-1]*n
d[0] = 0
M = []
for i in range(n):
    adj = list(map(int,input().split()))
    if adj[1] == 0:
        M += [[]]
    else:
        M += [adj[2:]]
Q = deque([0])

while Q != deque([]):
  u = Q.popleft()
  for i in range(len(M[u])):
    v = M[u][i]-1
    if d[v] == -1:
      d[v] = d[u] + 1
      Q.append(v)
for i in range(n):
  print(i+1,d[i])
                 
                 
  

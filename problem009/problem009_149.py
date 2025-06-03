
n = input()
d = [99999 for i in range(n)]
G = [0 for i in range(n)]
v = [[0 for i in range(n)] for j in range(n)]
   
def bfs(u):
  for i in range(n):
    if v[u][i] == 1:
      if d[i] > d[u] + 1:
         d[i] = d[u] + 1
         bfs(i)
    else:
      continue        
def _(): 
 d[0] = 0
 for i in range(n):
   bfs(i)
 for i in range(n):
   if d[i] == 99999:
      d[i] = -1
 for i in range(n):
   print '{0} {1}'.format(i+1, d[i])


for i in range(n):
  G = map(int, raw_input().split())
  for j in range(G[1]):
    v[G[0]-1][G[2+j]-1] = 1

_()
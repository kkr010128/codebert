import sys
sys.setrecursionlimit(10**9)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,M,L = map(int,readline().split())
ABC = [list(map(int,readline().split())) for _ in range(M)]
Q = int(readline())
ST = [list(map(int,readline().split())) for _ in range(Q)]
    
def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

INF = 10**11
d = [[INF]*N for i in range(N)] 
a =  [[INF]*N for i in range(N)] 
for x,y,z in ABC:
    if z <= L:
      d[x-1][y-1] = z
      d[y-1][x-1] = z
for i in range(N):
    d[i][i] = 0
    a[i][i] = 1
chk = warshall_floyd(d)

for i in range(N-1):
  for j in range(i+1,N):
    if chk[i][j] <= L:
      a[i][j] = 1
      a[j][i] = 1
ans = warshall_floyd(a)

for s,t in ST:
  answer = ans[s-1][t-1]
  if answer == INF:
      print(-1)
  else:
      print(answer-1)
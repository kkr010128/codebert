from scipy.sparse.csgraph import floyd_warshall
import sys
input = sys.stdin.readline
def solve():
  inf = float("Inf")
  n,m,l = (int(i) for i in input().split())
  path = [[-1*inf]*n for _ in range(n)]
  for i in range(m):
    a,b,c = (int(i) for i in input().split())
    path[a-1][b-1] = c
    path[b-1][a-1] = c
  d = floyd_warshall(path)
  q = int(input())
  minipath = [[-1*inf]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if d[i][j] <= l:
        minipath[i][j] = 1
  d2 = floyd_warshall(minipath)

  for i in range(q):
    s,t = (int(i) for i in input().split())
    s,t = s-1,t-1
    cost = d2[s][t]
    if cost == inf:
      print(-1)
    else:
      print(int(cost)-1)

solve()
import sys
input = sys.stdin.readline
N,M,L = map(int, input().split())
INF = float("inf")
dist1 = [[INF]*N for i in range(N)]
dist2 = [[INF]*N for i in range(N)]

for i in range(M):
  A,B,C = map(int, input().split())
  A -= 1
  B -= 1
  dist1[A][B] = C
  dist1[B][A] = C

for i in range(N):
  dist1[i][i] = 0
  dist2[i][i] = 0
  
for k in range(N):
  for i in range(N):
    for j in range(N):
      d = dist1[i][k]+dist1[k][j]
      if dist1[i][j] <= d:
        continue
      dist1[i][j] = d
for i in range(N):
  for j in range(N):
    if dist1[i][j] > L or i==j:
      continue
    dist2[i][j] = 1
  
for k in range(N):
  for i in range(N):
    for j in range(N):
      d = dist2[i][k]+dist2[k][j]
      if dist2[i][j] <= d:
        continue
      dist2[i][j] = d
Q = int(input())
for i in range(Q):
  s,t = map(int, input().split())
  print(dist2[s-1][t-1]-1 if dist2[s-1][t-1]<=L else -1)
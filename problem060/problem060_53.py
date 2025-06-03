n,m,l = map(int, input().split())
A = [[0 for j in range(m)] for i in range(n)]
B = [[0 for j in range(l)] for i in range(m)]
C = [[0 for j in range(l)] for i in range(n)]
for i in range(n):
  A[i] = list(map(int, input().split()))
for i in range(m):
  B[i] = list(map(int, input().split()))
for i in range(n):
  for j in range(l):
    for k in range(m):
      C[i][j] += A[i][k] * B[k][j]

for i in range(n):
  for j in range(l-1):
    print(C[i][j],end=' ')
  print(C[i][l-1],sep='')

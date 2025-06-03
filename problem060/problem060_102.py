def f():return map(int,raw_input().split())
n,m,l=f()
A = [f() for _ in [0]*n]
B = [f() for _ in [0]*m]
C = [[0 for _ in [0]*l] for _ in [0]*n]
for i in range(n):
  for j in range(l):
    print sum([A[i][k]*B[k][j] for k in range(m)]),
  print
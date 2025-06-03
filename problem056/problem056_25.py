def f():return map(int,raw_input().split())
n,m = f()
A = [f() for _ in [0]*n]
B = [input() for _ in [0]*m]
for i in range(n):
  print sum([A[i][j]*B[j] for j in range(m)])
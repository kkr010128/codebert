n = int(input())

A = [[] for i in range(n)]

for i in range(n):
  A[i] = list(map(int, input().split()))

f_inf = float("inf")
B = [[f_inf for i in range(2)] for j in range(n)]
B[0][1] = 0

for i in range(n):
  B[i][0] = i+1

def dbs(a):
  global order
  l = len(A[a-1])-2
  if l:
    for i in range(l):
      depth = B[a-1][1]+1
      b = A[a-1][i+2]
      if not b in order or depth < B[b-1][1]:
        B[b-1][1] = depth
        order.append(b)
        dbs(b)

order = [1]
dbs(1)

for i in range(n):
  if B[i][1] == f_inf:
    B[i][1] = -1
  print(" ".join(map(str, B[i])))

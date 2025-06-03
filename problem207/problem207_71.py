A = []
for i in range(3):
  A.append(list(map(int, input().split())))
B = [[0 for i in range(3)] for j in range(3)]
N = int(input())
for i in range(N):
  b = int(input())
  for j in range(3):
    for k in range(3):
      if A[j][k] == b:
        B[j][k] = 1
c = []
for i in range(3):
  c.append(B[i][0] & B[i][1] & B[i][2])
  c.append(B[0][i] & B[1][i] & B[2][i])
c.append(B[0][0] & B[1][1] & B[2][2])
c.append(B[0][2] & B[1][1] & B[2][0])
if sum(c) > 0:
  print("Yes")
else:
  print("No")
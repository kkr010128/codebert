# -*- coding: utf-8 -*-

A = [0] * 3
for i in range(3):
  A[i] = list(map(int, input().split()))
N = int(input())
b = []
for i in range(N):
  b.append(int(input()))


for b_i in b:
  for i in range(3):
    for j in range(3):
      if A[i][j] == b_i:
        A[i][j] = 0

if A[0][0] == 0 and A[0][1] == 0 and A[0][2] == 0:
  print('Yes')
elif A[1][0] == 0 and A[1][1] == 0 and A[1][2] == 0:
  print('Yes')
elif A[2][0] == 0 and A[2][1] == 0 and A[2][2] == 0:
  print('Yes')
elif A[0][0] == 0 and A[1][0] == 0 and A[2][0] == 0:
  print('Yes')
elif A[0][1] == 0 and A[1][1] == 0 and A[2][1] == 0:
  print('Yes')
elif A[0][2] == 0 and A[1][2] == 0 and A[2][2] == 0:
  print('Yes')
elif A[0][0] == 0 and A[1][1] == 0 and A[2][2] == 0:
  print('Yes')
elif A[0][2] == 0 and A[1][1] == 0 and A[2][0] == 0:
  print('Yes')
else:
  print('No')
A = list(map(int,input().split()))
B = list(map(int,input().split()))
T = int(input())

distance = abs(A[0] - B[0])

A[1] = A[1] * T
B[1] = B[1] * T

if distance <= (A[1] - B[1]):
  print('YES')
else:
  print('NO')
A, B, K = list(map(int, input().split()))
A -= K
if A < 0:
  B += A
  A = 0
if B < 0:
  B = 0
print(A, B)

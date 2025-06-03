A, B, K = [int(i) for i in input().split()]

if K <= A:
  print(A - K, B)
  exit(0)
if K <= (A + B):
  print(0, B - (K - A))
  exit(0)
else:
  print(0, 0)
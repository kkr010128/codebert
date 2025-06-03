A, B, N = map(int, input().split())
if N >= B - 1:
  print(int(A * (B - 1) / B))
else:
  print(int(A * N / B))
A, B, C, K=map(int, input().split())

if A>=K:
  print(K)
elif A+B>=K>A:
  print(A)
elif A+B+C>=K>A+B:
  print(A-(K-A-B))

A,B,K = list(map(int,input().split()))

if K <= A:
  print(A - K, B)

if A < K and K <= A + B:
  print(0, A + B - K)

if A + B < K:
  print(0, 0)
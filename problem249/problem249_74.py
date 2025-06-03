A, B, K= list(map(int, input().split()))

if A>= K:
  print(A-K, end=" ")
  print(B)
else:
  print(0, end=" ")
  print(max(B-(K-A),0))
A, B, K = map(int, input().split())

A_after = 0
B_after = 0

if A - K >= 0:
  A_after = A - K
  B_after = B

elif A + B - K >= 0:
  B_after = B - (K - A)
  
print(A_after, B_after)
A, B, K = map(int, input().split())
i = 0

if A <= K:
  K = K - A 
  A = 0
if A > K:
  A = A - K
  K = 0
if B <= K and A == 0:
  K = K - B
  B = 0
if B >= K and A == 0:
  B = B - K
  K = 0

print(A)
print(B)
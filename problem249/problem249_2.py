import sys
A, B, K= map(int, next(sys.stdin.buffer).split())
if K > A:
  a = 0
  b = max(0, B - (K - A))
else:
  a = A - K
  b = B

print(a, b)
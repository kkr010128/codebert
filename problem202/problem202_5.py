import math

N, A, B = map(int, input().split())
K = math.floor(N // (A + B))
blue = A * K
L = N % (A + B)
if L > A:
  blue += A
else:
  blue += L
print(blue)
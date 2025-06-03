import math

N = int(input())
ans = math.floor(N / 2)

if N % 2 == 0:
  print(ans - 1)
else:
  print(ans)
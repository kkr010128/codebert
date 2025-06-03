import math

N, M = map(int, input().split())

if N%2 == 1:
  a = 1
  b = N
  for i in range(M):
    print(a,b)
    a += 1
    b -= 1
else:
  m = N//2 - 1
  a = N//4
  b = a + 1
  c = N//2 + N//4
  d = c + 2
  for i in range(M):
    if i%2 == 0:
      print(a,b)
      a -= 1
      b += 1
    else:
      print(c,d)
      c -= 1
      d += 1 
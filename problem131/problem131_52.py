import math
a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

dist = abs(a-b)
pace = abs(v) - abs(w)

if pace <= 0:
  print('NO')
elif math.ceil(dist / pace) > t:
  print('NO')
else:
  print('YES')
import sys
rm = lambda: map(int, sys.stdin.buffer.readline().split())
ri = lambda: int(sys.stdin.readline())
a, v = rm()
b, w = rm()
t = ri()
if v - w == 0:
  print('NO')
  exit()
if 0 <= abs(a-b) / (v-w) <= t:
  print('YES')
else:
  print('NO')

